from flask import *

app = Flask(__name__)

@app.route('/post_data',methods=['GET','POST','DELETE'])
def post_data():
    if request.method == 'POST':

        result = request.form

        return render_template('get_data.html',dt = result)
    else:
        return render_template('post_data.html')

# @app.route('/get_data',methods = ['GET','DELETE'])
# def get_data():
#     if request.method == 'GET':
#         # uname = request.args.get('uname')
#         # passwrd = request.args.get('pass')
#         # print(uname, " ", passwrd)
#         return render_template('get_data.html')



@app.route('/success/<string:name>')
def success(name):
    return "Welcome, %s"%name

@app.route('/home/<string:name>')
def home(name):
    return render_template('home.html',name = name)



@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        if name != 'si':
            error = "invalid name"
            print(error)
        else:
            flash("you successfully logged in...")
            # return redirect(url_for('success',name=name))
            return redirect(url_for('home',name=name))

    return render_template('login.html',error=error)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'



app.debug = True
app.run()