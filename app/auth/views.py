from flask.templating import render_template
from . import auth
from app.forms import LoginForm

from flask import template_rendered


@auth.route('/login')
def login():
    context = {
        'login_form' : LoginForm()
    }

    return render_template('login.html', **context)
