import os
from datetime import datetime
from flask_mail import Message
from flask import render_template,redirect,request,url_for,make_response,session,flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from port import app,csrf,mail
from port.models import db,Contact
from port.form import ContactForm


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