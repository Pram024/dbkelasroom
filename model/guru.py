from app import db
from model.kelas import Kelasnya

class Gurunya(db.Model):
    __tablename__ = 'guru'

    id_guru = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    password = db.Column(db.String())
    full_name = db.Column(db.String())
    email = db.Column(db.String())
    alamat = db.Column(db.String())
    no_tlp = db.Column(db.Integer())
    kelas = db.relationship('Kelasnya')


    def __init__(self, user_name, password, full_name, email, alamat, no_tlp):
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.email = email
        self.alamat = alamat
        self.no_tlp = no_tlp

    def serialize(self):
        return {
            'id_guru':self.id_guru,
            'user_name':self.user_name,
            'password':self.password,
            'full_name':self.full_name,
            'email':self.email,
            'alamat':self.alamat,
            'no_tlp':self.no_tlp
        }