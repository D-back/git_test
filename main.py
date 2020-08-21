from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand

#导入自己的包
from user.views import user_dp
from goods.views import goods_dp
from libs.orm import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:961224@localhost:3306/work4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


manager = Manager(app)
#初始化 db 迁移工具
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#注册蓝图
app.register_blueprint(user_dp)
app.register_blueprint(goods_dp)

if __name__ == '__main__':
    manager.run()