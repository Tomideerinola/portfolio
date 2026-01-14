from flask_wtf import FlaskForm
from wtforms import StringField, EmailField,PasswordField,SubmitField,TelField,TextAreaField,FileField,DateField, RadioField,DecimalField,IntegerField,SelectField,MultipleFileField,SelectMultipleField
from wtforms.validators import DataRequired,Email,Length,EqualTo,Optional,NumberRange
from flask_wtf.file import FileAllowed,FileRequired


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = TelField("Phone Number", validators=[DataRequired(), Length(min=5, max=20)])
    message = TextAreaField('Message', validators=[DataRequired()])
    contact_method = RadioField('Preferred Contact Method',choices=[('call', 'Call'), ('text', 'Text')],validators=[DataRequired()])
    submit = SubmitField('Submit')
