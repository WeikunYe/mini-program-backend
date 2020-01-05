from db import db

#企业用户测试者
class OrgTesterModel(db.Model):
    
    __tablename__ = 'org_testers'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80))
    name = db.Column(db.String(80))
    gender = db.Column(db.String(1))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    test_by = db.Column(db.String(80))
    org_id = db.Column(db.Integer, db.ForeignKey('org_users.id'))
    
    def __init__(self, _id, phone, name, gender, height, weight, age, test_by, org_id):
        self.id = _id
        self.phone = phone
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight,
        self.age = age
        self.test_by = test_by
        self.org_id = org_id
    
    def json(self):
        return {
            'id': self.id,
            'phone': self.phone,
            'name': self.name,
            'gender': self.gender,
            'height': self.height,
            'weight': self.weight,
            'age': self.age,
            'test_by': self.test_by,
            'org_id': self.org_id
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
