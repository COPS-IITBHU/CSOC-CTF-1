from flask import Flask,request
from flask.templating import render_template
app=Flask(__name__,template_folder='.')

@app.route('/',methods=['GET','SHOW'])
def index():
    if request.method=='SHOW':
        return render_template('flag.txt')
    else:
        return render_template('index.html') 

if __name__=="__main__":
    app.run(host='0.0.0.0',port=4000)
