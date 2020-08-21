from flask import Blueprint
from flask import render_template

goods_dp = Blueprint('goods',__name__,url_prefix='/goods')
goods_dp.template_folder = '/templates'

@goods_dp.route('/index')
def index():
    return render_template('index.html')

@goods_dp.route('/info')
def info():
    return render_template('info.html')

@goods_dp.route('/goods_car')
def goods_car():
    return render_template('goods_car.html')
@goods_dp.route('/den_order')
def den_order():
    return render_template('den_order.html')
@goods_dp.route('/buy')
def buy():
    return render_template('buy.html')
