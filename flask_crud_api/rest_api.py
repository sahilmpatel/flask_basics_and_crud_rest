
from flask import *
from flask_mysqldb import MySQL


app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root@123'
app.config['MYSQL_DB'] = 'python_db1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/student',methods=['GET','POST'])
# show all student data .....
def student_show():

    try:
        conn = mysql.connection
        cur = conn.cursor()
        qry = "select * from student"

        cur.execute(qry)
        result = cur.fetchall()
        # print(result)
        return jsonify(result)
    except Exception as e:
        print(e)

    finally:
        cur.close()


@app.route('/student/add',methods=['GET','POST'])
# insert the new data ...
def add_student():
    try:
        conn = mysql.connection
        cur = conn.cursor()
        _json = request.json
        s_name = _json['name']
        s_id = _json['id']
        s_phone_no = _json['phone_no']
        s_class_id = _json['class_id']
        s_email = _json['email']
        in_qry = 'insert into student(name,id,phone_no,class_id,email)values(%s,%s,%s,%s,%s)'
        data = (s_name,s_id,s_phone_no,s_class_id,s_email)
        cur.execute(in_qry,data)
        conn.commit()
        resp = jsonify('Student added successfully!')
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()


@app.route('/student/<int:id>',methods=['POST','GET'])
# show by id

def show_student_by_id(id):

    try:

        conn = mysql.connection
        cur = conn.cursor()
        qry = 'select * from student where id=%s'
        val = (id,)
        cur.execute(qry,val)
        result = cur.fetchone()
        return jsonify(result)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        # conn.close()

@app.route('/student/update/<int:id>',methods=['POST'])
# update student data by id ..
def update_by_id(id):
    try:
        conn = mysql.connection
        cur = conn.cursor()

        _json = request.json
        s_name = _json['name']
        s_phone_no = _json['phone_no']
        s_email = _json['email']

        qry = 'update student set name=%s,phone_no=%s,email=%s where id=%s'
        data = (s_name,s_phone_no,s_email,id)
        cur.execute(qry,data)
        conn.commit()
        resp = jsonify('Student updated successfully!')
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
    #     # conn.close()


@app.route('/student/delete/<int:id>',methods=['POST','GET'])
def delete_by_id(id):
    try:
        conn = mysql.connection
        cur = conn.cursor()

        qry = 'delete from student where id=%s'
        val = (id,)

        cur.execute(qry,val)
        conn.commit()

        resp = jsonify('Student deleted successfully!')
        return resp
    except Exception as e:
        print(e)

    finally:
        cur.close()










@app.route('/rest',methods=['GET','POST'])
def rest():
    data  = "this first rest data.."
    return jsonify({'data':data})


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'



app.debug = True
app.run()