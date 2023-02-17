from flask import Flask
app = Flask(__name__)

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

DATABASE = 'recipes_db'

app.secret_key = "thisissecret"