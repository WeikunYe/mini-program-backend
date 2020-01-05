from flask_restful import Resource, reqparse
from flask import request

appID = "wx7c160012429ad408"
AppSecret = "b5a7175aad3252571af12a44204d1a68"
url_code = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={appid}&secret={appsecret}&code={code}&grant_type=authorization_code"
url_retoken = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid={appid}&grant_type=refresh_token&refresh_token={refresh_token}"
url_info = "https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}&lang=zh_CN"

class WxLogin(Resource):
    def post(self):
        arguments = request.form
        code = arguments['code']
        print('wx_code为：' + code)
        return {'code': 200, 'msg': '登录成功', 'uid': code}, 200