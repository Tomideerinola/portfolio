import os
from datetime import datetime
from flask_mail import Message
from flask import render_template,redirect,request,url_for,make_response,session,flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from port import app,csrf,mail
from port.models import db
from port.form import ContactForm


@app.get('/')
def home():
    return 'Test'