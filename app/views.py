from flask import Blueprint, render_template

views = Blueprint('main', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")