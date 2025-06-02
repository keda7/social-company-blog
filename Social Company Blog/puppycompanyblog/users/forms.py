# USERS/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords must match!")])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has already been registered!")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has already been registered!")

class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    def validate_email(self, field):
        if field.data != current_user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already in use by another account.")

    def validate_username(self, field):
        if field.data != current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError("This username is already in use by another account.")
