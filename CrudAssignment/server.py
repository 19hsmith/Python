from flask import Flask, render_template, request , redirect

from flask_app.controllers.friend_controller import Friend

from flask_app import app
   


if __name__ == "__main__":
    app.run(debug=True)

