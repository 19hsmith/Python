from flask_app import app
from flask import Flask , render_template , redirect , request
from flask_app.models.friends import Friend


@app.route("/")
def good_user():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_friend():
    Friend.save(request.form)
    return redirect('/user_data')

@app.route("/user_data")
def index():
    friends = Friend.get_all()
    return render_template("users.html",friends=friends)

@app.route('/delete_user/<int:id>')
def delete(id):
    Friend.delete({'id': id}) 
    return redirect('/user_data')

@app.route('/show_user/<int:id>')
def showinfo(id):
    usersdata=Friend.show({'id':id})
    print(usersdata)
    return render_template("singleuser.html", user=usersdata)

@app.route('/edit_user/<int:id>')
def editing(id):
    return render_template('editing.html',id=id)

@app.route('/edited/<int:id>',methods=['POST'])
def edited(id):
    print(request.form)
    Friend.edit(request.form)
    return redirect("/user_data")

        

            