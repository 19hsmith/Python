from flask_app import app
from flask import Flask , render_template , redirect , request,session, flash
from flask_app.models.bands import Band
from flask_app import bcrypt

@app.route('/delete_band/<int:id>')
def delete(id):
    Band.delete({'id': id}) 
    return redirect('/welcome_route')

@app.route('/show_band/<int:id>')
def bandinfo(id):
    bands=Band.get_band_with_user({'id': id})
    print(bands)
    if bands:
        return render_template("show_show.html", bands=bands)
    else:
        return redirect('/welcome_route')


@app.route('/edit_band/<int:id>')
def editing(id):
    band=Band.get_a_band({'id': id})
    print(band)
    return render_template('update_show.html',band=band)

@app.route('/edited/<int:id>',methods=['POST'])
def edited(id):
    if not Band.validate_music(request.form):
        return redirect(f'/edit_band/{id}')
    print(request.form)
    data = {
        **request.form,
        'id': id
    }
    Band.edit_band(data)
    return redirect("/welcome_route")

@app.route('/add_band')
def add_band():
    return render_template('/add_new_show.html' , bands = Band.get_band_info)

@app.route('/added_band' , methods = ['POST'])
def added_band():
    if not Band.validate_music(request.form):
        return redirect('/add_band')
    print(request.form)
    data = {
        ** request.form,
        'user_id':session['id']
    }
    print (session['id'])
    Band.create_band(data)
    return redirect('/logged_in')

@app.route('/welcome_route')
def return_route():
    bands = Band.get_band_info()
    return render_template("welcome.html" , bands = bands)