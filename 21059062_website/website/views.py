from flask import Blueprint, render_template

#defining blueprint of our application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")