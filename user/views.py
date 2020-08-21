from flask import Blueprint
from flask import render_template
from flask import redirect

from user.models import User

user_dp = Blueprint('user',__name__,url_prefix='/user')
user_dp.template_folder = './templates'


@user_dp.route('/register')
def register():
    return 'register.html'

@user_dp.route('/login')
def login():
    return render_template('login.html')
@user_dp.route('/info')
def info():
    return render_template('info.html')

@user_dp.route('/logout')
def logout():
    return redirect('/user/login')