from flask_app import app
from flask import Flask , render_template , redirect , request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def startpage():
    return render_template('index.html', dojos = Dojo.get_dojo_name())

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
   print(request.form)
   Dojo.create(request.form)
   return redirect('/')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    dojo = Ninja.show_ninjas({'id':id})
    print(dojo)
    return render_template('dojoshow.html' , dojo = dojo)








