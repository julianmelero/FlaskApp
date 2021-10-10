from flask import Flask, request, make_response, redirect, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "SUPER SECRETO"

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)



todos = ['Comprar Café', 'Enviar solicitud', 'Entregar Producto']

class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')



@app.route('/')
def index():
    user_ip= request.remote_addr
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip',user_ip)          
    session['user_ip'] = user_ip

    return response



@app.route('/hello')
def hello():
    #user_ip= request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {'user_ip':user_ip,
    'todos' : todos,
    'login_form': login_form,
    }
    return render_template('hello.html', **context)


if __name__ == "__main__":
    app.run(debug=True)