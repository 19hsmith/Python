from flask_app import app
from flask import Flask , render_template , redirect , request,session, flash
from flask_app.models.users import User
from flask_app import bcrypt


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register' , methods=['POST'])
def register():
    if not User.validate_new_user(request.form):
        return redirect('/')
    print(request.form)

    new_user = {
       **request.form,
       'password' :bcrypt.generate_password_hash(request.form['password'])
    }
    User.register(new_user)
    name = request.form['first_name']
    return redirect ('/')

@app.route('/log_in' , methods=['POST'])
def log_in():
    print(request.form)
    if User.validate_log_in(request.form):
        session['email'] = request.form['email']
        return redirect('/logged_in')
    else:
        return redirect('/')

@app.route('/logged_in')
def logged_in():
    if 'email' in session:
        user = User.welcome({'email':session['email']})
        print(user)
        return render_template('welcome.html',user = user)
    else:
        flash('Please enter an existing users details!' , 'log_in')
        return redirect('/')

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect('/')

@app.route('/registered/<name>')
def registered(name):
    return render_template('success.html' , name = name)