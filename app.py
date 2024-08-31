from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("index.html")
    
@app.route('/logout')
def logout():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8080)
