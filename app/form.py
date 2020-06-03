from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired
from flask_security.forms import RegisterForm, Required
from functions import freetime


class RecordForm(Form):
    mobile = StringField("Введите номер телефона", validators=[DataRequired()])
    service = SelectField("Выберите услугу", choices=[('Стрижка'), ('Стрижка с укладкой'), ('Стрижка бороды')])
    time = SelectField('Выберите время', choices=freetime())


class ExtendedRegisterForm(RegisterForm):
    username = StringField('Name', [Required()])
