from flask import  request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app.forms import LoginForm
from app import create_app

app = create_app()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)



todos = ['Comprar Café', 'Enviar solicitud', 'Entregar Producto']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/')
def index():
    user_ip= request.remote_addr
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip',user_ip)          
    session['user_ip'] = user_ip

    return response



@app.route('/hello', methods=['GET', 'POST'])
def hello():    
    #user_ip= request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    is_admin = session.get('is_admin')
    print(username)
    context = {'user_ip':user_ip,
    'todos' : todos,
    'login_form': login_form,
    'username': username,
    'is_admin': is_admin,
    }
    if login_form.validate_on_submit():            
        username = login_form.username.data
        
        if username == 'admin':
            session['is_admin'] = True

        session['username'] = username       
        flash('Nombre de usario registrado con éxito!') 
        return redirect(url_for('index'))

    return render_template('hello.html', **context)


if __name__ == "__main__":
    app.run(debug=True)