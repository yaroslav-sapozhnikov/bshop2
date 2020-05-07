from app import app
from flask import render_template

from form import RecordForm
from app import db
from flask import request
from flask import redirect
from flask import url_for
from flask_security import login_required
from models import Record
from flask_mail import Message

from app import mail
from flask_login import current_user
from app import security


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/record_page', methods=['POST', 'GET'])
@login_required
def record_page():
    form = RecordForm()
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        service = request.form.get('service')
        time = request.form.get('time')

        global dct
        dct = {'mobile': mobile, 'service': service, 'time': time}

        record = Record(mobile=mobile, service=service, time=time)
        db.session.add(record)
        db.session.commit()
        
        return redirect(url_for('success'))

    return render_template('record_page.html', form=form)


@app.route('/success')
@login_required
def success():
    service = dct['service']
    time = dct['time']
    mobile = dct['mobile']

    msg = Message("Новая запись", recipients=["flaskapp726@gmail.com"])
    msg.body = f'Время: {time}\nУслуга: {service}\nТелефон: {mobile}'
    mail.send(msg)

    msg = Message("Вы успешно записаны!", recipients=[current_user.email])
    msg.body = f'Время: {time}\nУслуга: {service}\nТелефон: {mobile}'
    mail.send(msg)

    return render_template('success.html', service=service, time=time)
