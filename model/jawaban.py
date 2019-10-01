from app import db
from model.v_kelas_jawaban import V_kelasnya

# from model.siswa import murid


class Jawabannya(db.Model):
    __tablename__ = 'jawaban'

    id_jawaban = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String())
    student_id = db.Column(db.Integer, db.ForeignKey('murid.id_siswa'))
    score = db.Column(db.Integer())
    classwork_id = db.Column(db.Integer, db.ForeignKey('tugas.id_tugas'))

    def __init__(self, answer, student_id, score, classwork_id ):
        self.answer = answer
        self.student_id = student_id
        self.score = score
        self.classwork_id = classwork_id

    def serialize(self):
        return {
            'id_jawaban':self.id_jawaban,
            'answer':self.answer,            
            'student_id':self.student_id,
            'score':self.score,
            'classwork_id':self.classwork_id
        }