import os
from flask import Flask, abort, session, request, redirect
from flask_cors import CORS, cross_origin
from server.model.board import Board

app = Flask(__name__, template_folder="../public", static_folder="../public", static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
board = Board('1')

from server.routes import *
from server.services import *

initServices(app)

if 'FLASK_LIVE_RELOAD' in os.environ and os.environ['FLASK_LIVE_RELOAD'] == 'true':
	import livereload
	app.debug = True
	server = livereload.Server(app.wsgi_app)
	server.serve(port=os.environ['port'], host=os.environ['host'])
