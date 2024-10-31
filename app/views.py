from flask import Blueprint, render_template, url_for

views = Blueprint('main', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/services')
def services():
    return render_template("services.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")