# noinspection PyUnresolvedReferences
from flask_wtf import FlaskForm
# noinspection PyUnresolvedReferences
from wtforms import StringField, BooleanField, SubmitField, PasswordField
# noinspection PyUnresolvedReferences
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = SubmitField("Ваш логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить")
    submit = SubmitField()
