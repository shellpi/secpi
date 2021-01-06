# Based in https://github.com/EbenKouao/pi-camera-stream-flask
# Adapted for SecPi

from flask import Flask, render_template, Response, request
from camera import Camera

from settings import *

import time
import threading
import os


# CAMERA #
pi_camera = Camera(flip=FLIP)


# APP #
app = Flask(__name__)


# INDEX #
@app.route('/<token>')
def index(token) -> any:
	return render_template('template/index/index.html')


# VIEWER #
@app.route('/view/<user>/<password>')
def view(user, password) -> any:
	if (USERS[user] == password) and (user != "" and password != ""):
		return render_template('template/viewer/index.html')
	else:
		return render_template('template/invalid_token/index.html')


# FRAME GENERATOR #
def gen(camera: Camera) -> any:
	#get camera frame
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
		       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/feed/<user>/<password>')
def feed(user, password): -> Response:
	if (USERS[user] == password) and (user != "" and password != ""):
		return Response(gen(pi_camera),
		                mimetype='multipart/x-mixed-replace; boundary=frame')
	else:
		return render_template('template/invalid_token/index.html')


if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=DEBUG)
