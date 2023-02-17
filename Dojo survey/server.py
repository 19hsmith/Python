from flask import Flask,render_template,redirect,session,request
app = Flask(__name__) 
app.secret_key = 'notasecretkey'   


@app.route('/')          
def hello_world():
    session.clear()
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def submitting():
    session['name'] = request.form.get('name')
    session['location'] = request.form.get('location')
    session['Favorite'] = request.form.get('Favorite')
    session['Comments'] = request.form.get('Comments')
    return redirect('/result')

@app.route('/result')
def finalProduct():
    return render_template('results.html')

if __name__=="__main__":   
    app.run(debug=True)  