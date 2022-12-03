from wtforms.form import Form
from wtforms.validators import IPAddress
from wtforms.fields import StringField

class RegisterAddressForm(Form):
    address = StringField('ip_address', validators=[IPAddress(ipv4=True)])