import os
from datetime import datetime
from flask_mail import Message
from flask import render_template,redirect,request,url_for,make_response,session,flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from port import app,csrf,mail
from port.models import db,Contact
from port.form import ContactForm


ADMIN_USERNAME = 'tomide'
ADMIN_PASSWORD = 'tomide2345'

@app.get('/')
def home():
    contact= ContactForm()

    return render_template('index.html',title="Home",contact=contact)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():

    contact= ContactForm()

    if request.method == 'POST':
        if contact.validate_on_submit():
            name= contact.name.data
            email = contact.email.data
            message= contact.message.data
            contact_method=contact.contact_method.data
            phone = contact.phone.data

            co=Contact(name=name,email=email,message=message,contact_method=contact_method,phone=phone)
            db.session.add(co)
            db.session.commit()
            flash('Your Message has been received and I will get back to you Shortly', 'success ')
            return redirect(url_for("contact"))
        else:
            flash('Please correct the errors in the form.', 'danger ')
    return render_template('index.html',contact=contact)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin_messages'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/admin/messages')
def admin_messages():
    # Security Check: Redirect to login if not authenticated
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    all_messages = Contact.query.order_by(Contact.date_sent.desc()).all()
    return render_template('admin_messages.html', messages=all_messages)

# Optional: Route to update status from 'unattended' to 'read'
@app.route('/admin/mark_read/<int:id>')
def mark_read(id):
    msg = Contact.query.get_or_404(id)
    msg.contact_status = "attended"
    db.session.commit()
    return redirect(url_for('admin_messages'))