from flask import Flask
from flask import request
from flask_bootstrap import Bootstrap
from flask import render_template
app = Flask(__name__)
Bootstrap(app)
from forms import LoginForm
from config import Config
app.config.from_object(Config)
from mysql_tool import mysql


@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username':'sunlight'}
    form = LoginForm()
    return render_template("index.html",title='登 录',form=form)
@app.route('/lognin_request',methods=['POST'])
def login_request():
    ms = mysql()
    user = request.form['username'];
    password = request.form['password'];
    print("user:"+user)
    print("password:" + password)
    if ms.get_user(user,password):
        return "1"
    else:
        return '0'
@app.route('/login')
def login():
    #创建一个表单实例
    form = LoginForm()
    return render_template('login.html',title='登 录',form=form)

if __name__ == '__main__':
    app.run()
