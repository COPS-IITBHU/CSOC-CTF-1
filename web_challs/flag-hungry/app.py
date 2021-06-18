from flask import Flask
from flask.templating import render_template

app=Flask(__name__,template_folder='.')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thengotoflagshop')
def show_flag():
    return 'csoc{sh0p_1s_Cl0s3d}'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=3000)