from flask_app import app
from flask import Flask , render_template , redirect , request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/add_ninja')
def added_ninja():
    return render_template('/addninja.html' , dojos = Dojo.get_dojo_name())

@app.route('/added_ninja' , methods=['POST'])
def add_ninja():
    print(request.form)
    Ninja.create_ninja(request.form)
    return redirect('/')



