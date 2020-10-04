"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional, Email

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField( "Username", validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField( "Password", validators=[InputRequired(), Length(min=6, max=55)],)


class RegisterForm(FlaskForm):
    """User registration form."""

    username = StringField( "Username", validators=[InputRequired(), Length(min=1, max=20)], )
    password = PasswordField( "Password", validators=[InputRequired(), Length(min=6, max=55)],)
    email = StringField( "Email", validators=[InputRequired(), Email(), Length(max=50)],)
    first_name = StringField( "First Name", validators=[InputRequired(), Length(max=30)],)
    last_name = StringField( "Last Name", validators=[InputRequired(), Length(max=30)],)


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()],)
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],)
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)],)


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)],)
    available = BooleanField("Available?")
