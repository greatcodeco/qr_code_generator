from wtforms import Form, StringField, validators

class inputForm(Form):
    address = StringField('Tanımlamak istediğiniz adres', [validators.DataRequired(), validators.Length(min=1, max=1000)])