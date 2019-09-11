from app import db

class Kelasnya(db.Model):
    __tablename__ = 'kelas'

    id_kelas = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String())
    teacher = db.Column(db.Integer, db.ForeignKey('guru.id_guru'))

    # movies = db.relationship('Movies')

    def __init__(self, class_name, teacher, ):
        self.class_name = class_name
        self.teacher = teacher

    
    def serialize(self):
        return {
            'id_guru':self.id_guru,
            'class_name':self.class_name,
            'teacher':self.teacher
        }