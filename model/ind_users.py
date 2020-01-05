from db import db

#个人用户
class IndUserModel(db.Model):
    
    __tablename__ = 'ind_users'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80))
    name = db.Column(db.String(80))
    gender = db.Column(db.String(1))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    remain = db.Column(db.Integer)
    
    # id: 微信uid，gender M/F，height cm，weight g，remain 剩余测试数量
    def __init__(self, _id, phone, name, gender, height, weight, age, remain):
        self.id = _id
        self.phone = phone
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = height
        self.age = age
        self.remain = remain
    
    # json个人用户
    def json(self):
        return{
            'id': self.id,
            'phone': self.phone,
            'name': self.name,
            'gender': self.gender,
            'height': self.height,
            'weight': self.weight,
            'age': self.age,
            'remain': self.remain
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    #用户充值
    def top_up(self, count):
        self.remain = self.remain + count
    
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
