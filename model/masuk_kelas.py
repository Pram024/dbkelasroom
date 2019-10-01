from app import db

class MasukKelasnya(db.Model):
    __tablename__ = 'masuk_kelas'

    id_masuk_kelas = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('murid.id_siswa'))
    class_id = db.Column(db.Integer, db.ForeignKey('kelas.id_kelas'))

    # movies = db.relationship('Movies')

    def __init__(self, student_id, class_id ):
        self.student_id = student_id
        self.class_id = class_id

    def serialize(self):
        return {
            'id_masuk_kelas':self.id_masuk_kelas,
            'student_id':self.student_id,
            'class_id':self.class_id
        }