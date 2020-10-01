from flask import render_template, redirect
from flask_login import login_required
from . import main

@main.route('/')
def index():
    return render_template('index.html')