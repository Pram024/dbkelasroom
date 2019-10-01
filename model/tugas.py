from app import db
from model.jawaban import Jawabannya
from model.v_kelas_jawaban import V_kelasnya

class Tugasnya(db.Model):
    __tablename__ = 'tugas'

    id_tugas = db.Column(db.Integer, primary_key=True)
    kelas_id = db.Column(db.Integer, db.ForeignKey('kelas.id_kelas'))
    question = db.Column(db.String())
    answer_teacher = db.Column(db.String())

    def __init__(self, kelas_id, question, answer_teacher ):
        self.kelas_id = kelas_id
        self.question = question
        self.answer_teacher = answer_teacher

    def serialize(self):
        return {
            'id_tugas':self.id_tugas,
            'kelas_id':self.kelas_id,
            'question':self.question,
            'answer_teacher':self.answer_teacher
        }