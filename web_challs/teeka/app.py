from sqlite3.dbapi2 import Row
from flask import *
import sqlite3

app=Flask(__name__,template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        usrname=request.form['usrname']
        password=request.form['password']
        con=sqlite3.connect('usersDB.db')
        cur=con.cursor()
        cur.execute(f"select usrname from users where usrname='{usrname}' and password='{password}'")
        rows=cur.fetchall()
        con.close()
        if rows:
            return render_template('flag.txt')
        else:
            return render_template('login_failed.html')
        

if __name__=="__main__":
    app.run(host='0.0.0.0',port=1669)
