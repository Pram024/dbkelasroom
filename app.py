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
        for user in siswa:
            if user.user_name == body ["user_name"] and user.password == body ["password"]:
                return jsonify({
                    "message":"LOOGIN BERHASIL",
                    "id_siswa":user.id_siswa
                    })
        return jsonify({
            "message":"LOOGIN GAGAL",
            "data":[]
            })
    except Exception as e :
        return jsonify(str(e)), 500

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
        for user in guru:
            if user.user_name == body ["user_name"] and user.password == body ["password"]:
                return jsonify({
                    "message":"LOOGIN BERHASIL",
                    "id_guru":user.id_guru
                    })
        return jsonify({
            "message":"LOOGIN GAGAL",
            "data":[]
            })
    except Exception as e :
        return jsonify(str(e)), 500