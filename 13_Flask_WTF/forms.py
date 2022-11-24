from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, RadioField, SelectField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField("Name Of Student", [DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")
    email = EmailField('Email', validators=[DataRequired("Please enter your email address.")])
    Age = IntegerField("age", [DataRequired("Please enter your age.")])
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")
