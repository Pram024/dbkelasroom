from app import db

class V_kelasnya(db.Model):
    __tablename__ = 'v_kelas_jawab'

    id_jawaban = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer())
    id_tugas = db.Column(db.Integer, db.ForeignKey('tugas.id_tugas'))
    id_kelas = db.Column(db.Integer, db.ForeignKey('kelas.id_kelas'))
    class_name = db.Column(db.String())
    score = db.Column(db.Integer())

    def __init__(self, student_id, id_tugas, id_kelas, class_name, score ):
        self.student_id = student_id
        self.id_tugas = id_tugas
        self.id_kelas = id_kelas
        self.class_name = class_name
        self.score = score

    def serialize(self):
        return {
            # 'id':self.id,
            'student_id':self.student_id,
            'id_tugas':self.id_tugas,
            'id_kelas':self.id_kelas,
            'class_name':self.class_name,
            'score':self.score
        }