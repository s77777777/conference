from flask import Blueprint, request, render_template, session, redirect


from .. import db
from .. import models
from .. import forms

blue_account = Blueprint('blue_user', __name__, template_folder='templates')


@blue_account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = forms.LoginForm()
        return render_template('login.html', form=form)

    else:
        form = forms.LoginForm(formdata=request.form)
        error_msg = ''
        if form.validate():
            res = db.session.query(models.UserInfo).filter(models.UserInfo.name == form.data['name'],
                                                           models.UserInfo.password == form.data['password']).first()
            if res:
                session['user_info'] = res.name,
                session['user_id'] = res.id
                return redirect('/conference')
            else:
                error_msg = '账户或密码错误'

        return render_template('login.html', form=form, error_msg=error_msg)
