#flask runner

from flask import Flask, render_template
from flask import request, make_response
from flask_cors import CORS



app = Flask('testapp', static_url_path='/static')
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)



@app.route('/', methods=['GET'])


def get_index():
	response = make_response(render_template('index.html'))
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response
	








app.run(port=8000)