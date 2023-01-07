from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
""" Create an instance of Flask """
app = Flask(__name__)
CORS(app)
""" Create an instance of MySQL"""
mysql = MySQL()

""" Create an instance of Flask RESTful API"""
api = Api(app)

""" Set database credentials in config."""
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'students'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

""" Initialize the MySQL extension"""
mysql.init_app(app)



class StudentList(Resource):


    """get all student"""
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM `student`""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    """create new student"""
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _code = str(request.form['code'])
            _birthday = str(request.form['birthday'])
            _address = str(request.form['address'])
            _classId = int(request.form['classId'])
            _status = int(request.form['status'])
            _sex = int(request.form['sex'])
            create_user_cmd = """INSERT INTO `student`( `name`, `code`, `birthday`, `address`, `classId`,`status`,`sex`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(create_user_cmd, (
                _name, _code, _birthday, _address, _classId, _status, _sex))
            conn.commit()
            response = jsonify(
                message='Student added successfully.', id=cursor.lastrowid)
            # response.data = cursor.lastrowid
            response.status_code = 201
        except Exception as e:
            print(e)
            response = jsonify('Failed to add student.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)




class Student(Resource):
    """get student by id"""
    def get(self, student_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM `student` WHERE `id`=%s""", (student_id))
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    """update student by id"""
    def put(self, student_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _code = str(request.form['code'])
            _birthday = str(request.form['birthday'])
            _address = str(request.form['address'])
            _classId = int(request.form['classId'])
            _status = int(request.form['status'])
            _sex = int(request.form['sex'])
            update_user_cmd = """UPDATE `student` SET `name`=%s,`code`=%s,`birthday`=%s,`address`=%s,`classId`=%s,`status`=%s,`sex`=%s WHERE `id`=%s"""
            cursor.execute(update_user_cmd, (_name, _code,
                           _birthday, _address, _classId, _status, _sex, student_id))
            conn.commit()
            response = jsonify('User updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update user.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)
    """delete student by id"""
    def delete(self, student_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM `student` WHERE `id`=%s""", (student_id))
            conn.commit()
            response = jsonify('User deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete user.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)



class ClassList(Resource):
    """get list class"""
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM `class`""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    """create new class"""
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _year = str(request.form['year'])
            _note = str(request.form['note'])
            _status = int(request.form['status'])
            create_class_cmd = """INSERT INTO `class`( `name`, `year`, `note`,`status`) VALUES (%s,%s,%s,%s)"""
            cursor.execute(create_class_cmd, (
                _name, _year, _note,_status))
            conn.commit()
            response = jsonify(
                message='Class added successfully.', id=cursor.lastrowid)
            # response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add class.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)



class Class(Resource):
    """get  class by id"""
    def get(self, class_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM `class` WHERE `id`=%s""", (class_id))
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    """update  class by id"""
    def put(self, class_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _year = str(request.form['year'])
            _note = str(request.form['note'])
            _status = int(request.form['status'])
            update_user_cmd = """UPDATE `class` SET `name`=%s,`year`=%s,`note`=%s,`status`=%s WHERE `id`=%s"""
            cursor.execute(update_user_cmd, (_name, _year,
                           _note, _status, class_id))
            conn.commit()
            response = jsonify('Class updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update Class.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)
    """delete  class by id"""
    def delete(self, class_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM `class` WHERE `id`=%s""", (class_id))
            conn.commit()
            response = jsonify('class deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete class.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


"""API resource routes"""
api.add_resource(StudentList, '/students', endpoint='students')
api.add_resource(Student, '/student/<int:student_id>', endpoint='student')
api.add_resource(ClassList, '/classes', endpoint='classes')
api.add_resource(Class, '/class/<int:class_id>', endpoint='class')

if __name__ == "__main__":
    app.run(debug=True)
