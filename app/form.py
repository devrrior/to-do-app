from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Length
from app.models import User


# def length_honeypot(form, field):
#         if len(field.data) > 0:
#                 raise validators.ValidationError("Area must be empty")

class SignupForm(FlaskForm):
    email = StringField("Email",validators=[
        DataRequired(),
        Email()
    ])
    username = StringField("Username",validators=[
        Length(max=30,min=3),
        DataRequired()
    ])
    password= PasswordField("Password",validators=[
        DataRequired()
    ])
    submit = SubmitField("Submit")


    def validate_username(self,username):
        if User.get_by_username(username.data):
            raise validators.ValidationError("User not available.")

    def validate_email(self,email):
        if User.get_by_email(email.data):
            raise validators.ValidationError("Email not available.")

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[
        DataRequired(),
    ])
    password= PasswordField("Password",validators=[
        DataRequired()
    ])
    submit = SubmitField("Submit")
