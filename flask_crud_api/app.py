from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi home'
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index/<int:pk>')
def show_id(pk):
    return 'id is:%d'%pk

def same():
    return 'same as django urls....'

app.add_url_rule('/same','same',same) # just like django urls.py


@app.route('/admin')
def admin():
    return 'admin'


@app.route('/librarion')
def librarion():
    return 'librarion'


@app.route('/student')
def student():
    return 'student'


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'librarion':
        return redirect(url_for('librarion'))
    if name == 'student':
        return redirect(url_for('student'))

# ..........using some dummy data ........

data = [
    {'id':1,'name':'alex'},
    {'id':2,'name':'elliot'},
]
@app.route('/dummy')
def dummy():

    return render_template('dummy.html',dt=data)

if __name__ == '__main__':
    app.run(debug=True)