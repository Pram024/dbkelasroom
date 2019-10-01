from app import db
from model.jawaban import Jawabannya
from model.masuk_kelas import MasukKelasnya
from model.myclass import MyClassnya
from model.myclass2 import MyClass2nya



class Siswanya(db.Model):
    __tablename__ = 'murid'

    id_siswa = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    password = db.Column(db.String())
    full_name = db.Column(db.String())
    email = db.Column(db.String())
    alamat = db.Column(db.String())
    no_tlp = db.Column(db.Integer())

    masuk_kelas = db.relationship('MasukKelasnya')

    def __init__(self, user_name, password, full_name, email, alamat, no_tlp):
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.email = email
        self.alamat = alamat
        self.no_tlp = no_tlp

    
    def serialize(self):
        return {
            'id_siswa':self.id_siswa,
            'user_name':self.user_name,
            'password':self.password,
            'full_name':self.full_name,
            'email':self.email,
            'alamat':self.alamat,
            'no_tlp':self.no_tlp
        }