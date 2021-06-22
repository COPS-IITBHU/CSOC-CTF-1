from flask import Flask,request
from flask.templating import render_template_string

app=Flask(__name__,template_folder='.')

@app.route('/<name>')
def index(name):
    return render_template_string(name)

@app.errorhandler(404)
def funcerr(err):
    # content=request.args.get('cool')
    # con='''Could not find ''' %(content)
    strings="Lol 404, looks like flask is working as intended."
    return strings ,404
if __name__=="__main__":
    app.run(host="0.0.0.0",port=1634)