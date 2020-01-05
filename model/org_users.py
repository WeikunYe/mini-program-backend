from db import db
from werkzeug.security import generate_password_hash, check_password_hash

#企业用户
class OrgUserModel(db.Model):
    
    __tablename__ = 'org_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password_hash = db.Column(db.String)
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))
    testers = db.relationship('OrgTesterModel', lazy='dynamic')
    
    def __init__(self, _id, username, password, phone, email):
        self.id = _id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.phone = phone
        self.email = email
    
    def json(self):
        return {
            'id': self.id,
            'username': self.username
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
