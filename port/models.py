from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text, nullable=False)
    contact_method = db.Column(db.String(20), nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)
    contact_status = db.Column(db.String(50), default="unattended")  