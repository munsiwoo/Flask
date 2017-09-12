#-*- coding:utf-8 -*-
# render_template
from flask import (Flask, render_template)

app = Flask(__name__)

@app.route('/<name>')
def hello(name=None) :
	return render_template('index.html', name=name)

if(__name__ == '__main__') :
	app.run()