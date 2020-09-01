from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
@login_required
def home():
    return render_template('home.html')

@main.route('/new_analysis', methods=['POST', 'GET'])
@login_required
def new_analysis():
    if request.method == 'POST':
        print(request.form['info3'])
    return render_template('new_analysis.html', name=current_user.name)
