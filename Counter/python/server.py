# pair programmed with jacob and luis
from flask import Flask, render_template, request, redirect, session  # added render_template!

app = Flask(__name__)                     
app.secret_key = 'keyword1' 


@app.route('/')
def countUp():
    if 'refreshCount' not in session:
        session["refreshCount"] = 0
    session['refreshCount'] +=1 
    return render_template('index.html')





@app.route('/destroy_session',methods=['GET','POST'])                           
def destroy():
    session.clear()
    return redirect('/')

@app.route('/upTwo',methods=['GET','POST'])
def upTwo():
    session['refreshCount'] += 1
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)    