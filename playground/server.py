from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def three():
    return render_template("index.html",x=3,col = 'blue')
@app.route('/play/<x>')
def five(x):
    return render_template("index.html",x=int(x),col = 'blue')
@app.route('/play/<x>/<col>')
def color(x,col):
    return render_template("index.html",x=int(x),col = col)



if __name__=="__main__":
    app.run(debug=True)

