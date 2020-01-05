from flask import Flask, request, make_response
import json
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db import db
from resources.ind_users import IndUser
from resources.wx_login import WxLogin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://jwj:jhfhfd^&*178D@120.79.236.242/mini_program?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(IndUser, '/ind_user/<string:phone>')
api.add_resource(WxLogin, '/login')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
