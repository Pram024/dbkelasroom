from app import db
from model.tugas import Tugasnya
from model.masuk_kelas import MasukKelasnya
from model.myclass import MyClassnya
from model.myclass2 import MyClass2nya
from model.v_kelas_jawaban import V_kelasnya



class Kelasnya(db.Model):
    __tablename__ = 'kelas'

    id_kelas = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String())
    teacher = db.Column(db.Integer, db.ForeignKey('guru.id_guru'))

    tugas = db.relationship('Tugasnya')
    masuk_kelas = db.relationship('MasukKelasnya')

    def __init__(self, class_name, teacher ):
        self.class_name = class_name
        self.teacher = teacher

    def serialize(self):
        return {
            'id_kelas':self.id_kelas,
            'class_name':self.class_name,
            'teacher':self.teacher
        }