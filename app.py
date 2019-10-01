from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user'  : 'postgres',
    'pw'    : 'postgres',
    'db'    : 'kelasroom',
    'host'  : 'localhost',
    'port'  : '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
from model.siswa import Siswanya
from model.guru import Gurunya
from model.kelas import Kelasnya
from model.tugas import Tugasnya
from model.jawaban import Jawabannya
from model.masuk_kelas import MasukKelasnya
from model.myclass import MyClassnya
from model.myclass2 import MyClass2nya
from model.v_kelas_jawaban import V_kelasnya


@app.route('/')
def main():
    return 'Selamat datang di kelasroom'

@app.route('/registers', methods=['POST'])
def register_siswa():
    body = request.json
    siswaData = Siswanya.query.all()
    statusCode = 200

    for user in siswaData:
        print(user.serialize()['user_name'])
        if body["email"] in (user.serialize()['email']):
            statusCode = 400
            return jsonify("email telah digunakan")
            break
        elif  body["user_name"] in (user.serialize()['user_name']):
            statusCode = 400
            return jsonify("user name telah digunakan")
            break
    if statusCode == 200:
        try :
            siswa = Siswanya(body['user_name'], body['password'], body['full_name'], body['email'], body['alamat'],body['no_tlp'])
            db.session.add(siswa)
            db.session.commit()
            return jsonify({
                'id_siswa': siswa.id_siswa
            })
        except Exception as e :
            return jsonify(str(e)), 500
        finally:
            db.session.close()

@app.route('/allsiswa', methods=['GET'])
def get_all_siswa():
    try:
        siswa = Siswanya.query.all()
        return jsonify({'siswa': [mbr.serialize() for mbr in siswa]})
    except Exception as e:
        return jsonify(str(e))

@app.route('/siswa/<id_>', methods=['GET'])
def get_siswa_by_id(id_) :
    try :
        siswa = Siswanya.query.filter_by(id_siswa=id_).first()
        return jsonify(siswa.serialize())
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/loginsiswa', methods=['POST'])
def login_siswa():
    try:
        body =  request.json
        siswa = Siswanya.query.all()
        statusCode = 400
        for user in siswa:
            if user.user_name == body ["user_name"] and user.password == body ["password"]:
                statusCode = 200
                return jsonify({
                    "message":"LOOGIN BERHASIL",
                    "id_siswa":user.id_siswa
                    })
        return jsonify({
            "message":"LOOGIN GAGAL",
            "data":[]
            }) , statusCode
    except Exception as e :
        return jsonify(str(e))

@app.route('/registerguru', methods=['POST'])
def register_guru():
    body = request.json
    guruData = Gurunya.query.all()
    statusCode = 200

    for user in guruData:
        print(user.serialize()['user_name'])
        if body["email"] in (user.serialize()['email']):
            statusCode = 400
            return jsonify("email telah digunakan")
            break
        elif  body["user_name"] in (user.serialize()['user_name']):
            statusCode = 400
            return jsonify("user name telah digunakan")
            break
    if statusCode == 200:
        try :
            guru = Gurunya(body['user_name'], body['password'], body['full_name'], body['email'], body['alamat'],body['no_tlp'])
            db.session.add(guru)
            db.session.commit()
            return jsonify({
                'id_guru': guru.id_guru
            })
        except Exception as e :
            return jsonify(str(e)), 500
        finally:
            db.session.close()

@app.route('/allguru', methods=['GET'])
def get_all_guru():
    try:
        guru = Gurunya.query.all()
        return jsonify({'guru': [mbr.serialize() for mbr in guru]})
    except Exception as e:
        return jsonify(str(e))

@app.route('/guru/<id_>', methods=['GET'])
def get_guru_by_id(id_) :
    try :
        guru = Gurunya.query.filter_by(id_guru=id_).first()
        return jsonify(guru.serialize())
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/loginguru', methods=['POST'])
def login_guru():
    try:
        body =  request.json
        guru = Gurunya.query.all()
        statusCode = 400
        for user in guru:
            if user.user_name == body ["user_name"] and user.password == body ["password"]:
                statusCode = 200
                return jsonify({
                    "message":"LOOGIN BERHASIL",
                    "id_guru":user.id_guru
                    })
        return jsonify({
            "message":"LOOGIN GAGAL",
            "data":[]
            }), statusCode
    except Exception as e :
        return jsonify(str(e))

@app.route('/registerkelas', methods=['POST'])
def register_kelas():
    body = request.json
    kelasData = Kelasnya.query.all()
    statusCode = 200

    for user in kelasData:
        print(user.serialize()['class_name'])
        if body["class_name"] in (user.serialize()['class_name']):
            statusCode = 400
            return jsonify("nama kelas telah digunakan")
            break
    if statusCode == 200:
        try :
            kelas = Kelasnya(body['class_name'], body['teacher'])
            db.session.add(kelas)
            db.session.commit()
            return jsonify({
                'id_kelas': kelas.id_kelas
            })
        except Exception as e :
            return jsonify(str(e)), 500
        finally:
            db.session.close()

@app.route('/allclass', methods=["GET"])
def getAllClass():
    try:
        kelas = Kelasnya.query.all()
        return jsonify({'kelas': [mbr.serialize() for mbr in kelas]})
    except Exception as e:
        return jsonify(str(e))

@app.route('/kelas/<id_>', methods=['GET'])
def get_kelas_by_id(id_) :
    try :
        kelas = Kelasnya.query.filter_by(id_kelas=id_).first()
        return jsonify(kelas.serialize())
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/registertugas', methods=['POST'])
def register_tugas():
    body = request.json
    tugasData = Tugasnya.query.all()
    statusCode = 200

    # for user in tugasData:
    #     print(user.serialize()['kelas_id'])
    #     if body["id_tugas"] in (user.serialize()['id_tugas']):
    #         statusCode = 400
    #         return jsonify("nama tugas telah digunakan")
    #         break
        
    if statusCode == 200:
        try :
            tugas = Tugasnya(body['kelas_id'], body['question'], body['answer_teacher'])
            db.session.add(tugas)
            db.session.commit()
            return jsonify({
                'id_tugas': tugas.id_tugas
            })
        except Exception as e :
            return jsonify(str(e)), 500
        finally:
            db.session.close()

@app.route('/alltugas', methods=["GET"])
def getAlltugas():
    try:
        tugas = Tugasnya.query.all()
        return jsonify({'tugas': [mbr.serialize() for mbr in tugas]})
    except Exception as e:
        return jsonify(str(e))

@app.route('/tugas/<id_>', methods=['GET'])
def get_tugas_by_id(id_) :
    try :
        tugas = Tugasnya.query.filter_by(id_tugas=id_).first()
        return jsonify(tugas.serialize())
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/registerjawaban', methods=['POST'])
def register_jawaban():
    body = request.json
    jawabanData = Jawabannya.query.all()
    statusCode = 200
    # tugasData = json.load(get_tugas_by_id(body['classwork_id']))
    tugasData = Tugasnya.query.filter_by(id_tugas=body['classwork_id']).first().serialize()
    print(tugasData)
    # for user in jawabanData:
    #     if body["classwork_id"] in (user.classwork_id) and body["student_id"] in (user.student_id):
    #         statusCode = 400
    #         return jsonify("anda sudah menjawab pertanyaan inih")
    #         break   
    if statusCode == 200:
        if body["answer"] == tugasData["answer_teacher"]:
            score = 10
        else:
            score = 0
        try :
            jawaban = Jawabannya(body['answer'],body['student_id'], score, body['classwork_id'])
            db.session.add(jawaban)
            db.session.commit()
            return jsonify({
                'id_jawaban': jawaban.id_jawaban
            })
        except Exception as e :
            return jsonify(str(e)), 500
        finally:
            db.session.close()

@app.route('/alljawaban', methods=["GET"])
def getAlljawaban():
    try:
        jawaban = Jawabannya.query.all()
        return jsonify({'jawaban': [mbr.serialize() for mbr in jawaban]})
    except Exception as e:
        return jsonify(str(e))

@app.route('/jawaban/<id_>', methods=['GET'])
def get_jawaban_by_id(id_) :
    try :
        jawaban = Jawabannya.query.filter_by(id_jawaban=id_).first()
        return jsonify(jawaban.serialize())
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/masukkelas', methods=['POST'])
def register_masukkelas():
    body = request.json
    masukkelasData = MasukKelasnya.query.all()
    statusCode = 200
        
    if statusCode == 200:
        try :
            masukkelas = MasukKelasnya(body['student_id'],body['class_id'])
            db.session.add(masukkelas)
            db.session.commit()
            return jsonify({
                'id_masuk_kelas': masukkelas.id_masuk_kelas
            })
        except Exception as e :
            return jsonify(str(e)), 500
        finally:
            db.session.close()

@app.route('/allmasukkelas', methods=["GET"])
def getAllmasukkelas():
    try:
        masukkelas = MasukKelasnya.query.all()
        return jsonify({'masukkelas': [mbr.serialize() for mbr in masukkelas]})
    except Exception as e:
        return jsonify(str(e))

@app.route('/masukkelas/<id_>', methods=['GET'])
def get_masukkelas_by_id(id_) :
    try :
        masukkelas = MasukKelasnya.query.filter_by(id_masuk_kelas=id_).first()
        return jsonify(masukkelas.serialize())
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/kelasguru/<id_>', methods=['GET'])
def get_kelasguru_by_id(id_) :
    try :
        kelas = Kelasnya.query.filter_by(teacher=id_).all()
        return jsonify({'kelas': [mbr.serialize() for mbr in kelas]})
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/myclass/<id_>', methods=['GET'])
def get_myclass(id_) :
    try :
        myclass = MyClassnya.query.filter_by(student_id=id_).all()
        print(myclass)
        return jsonify({'myclass': [mbr.serialize() for mbr in myclass]})
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/kelasjoin/<id_>', methods=['GET'])
def get_kelasjoin(id_) :
    try :
        myclass = MyClass2nya.query.filter_by(class_id=id_).all()
        print(myclass)
        response = {'myclass': [mbr.serialize() for mbr in myclass]}
        return jsonify(response)
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/mysoal/<id_>', methods=['GET'])
def get_mysoal(id_) :
    try :
        mysoal = Tugasnya.query.filter_by(kelas_id=id_).all()
        print(mysoal)
        return jsonify({'mysoal': [mbr.serialize() for mbr in mysoal]})
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/jawabmurid/<id_>', methods=['GET'])
def get_jawabmurid(id_) :
    try :
        jawabmurid = Jawabannya.query.filter_by(student_id=id_).all()
        print(jawabmurid)
        return jsonify({'jawabmurid': [mbr.serialize() for mbr in jawabmurid]})
    except Exception as e :
        return jsonify(str(e)), 500

@app.route('/scorenya/<id_>', methods=['GET'])
def get_scorenya(id_) :
    try :
        scorenya = V_kelasnya.query.filter_by(student_id=id_).all()
        print(scorenya)
        return jsonify({'scorenya': [mbr.serialize() for mbr in scorenya]})
    except Exception as e :
        return jsonify(str(e)), 500