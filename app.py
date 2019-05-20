from flask import Flask, render_template, request
from forms import inputForm
import pyqrcode
import os
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linuxdegilgnulinux'

@app.route('/')
def home():
    form = inputForm(request.form)
    return render_template('index.html', form=form)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = inputForm(request.form)
    if request.method == 'POST' and form.validate():
        address = request.form.get('address')
        url = pyqrcode.create(address)
        url.png('static/url.png', scale=8)
        return render_template('index.html', form=form, address=address)
    return render_template('index.html', form=form, address=address)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
