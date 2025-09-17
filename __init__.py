import flask
from start import *

app =flask.Flask(__name__)

@app.route('/')
def hi():
    return flask.render_template('Main.html',
    path= 'main')

@app.route('/start')
def start():
    main_start()
    return flask.render_template('start.html',
    path= 'start',
    families = Familias)
app.run()