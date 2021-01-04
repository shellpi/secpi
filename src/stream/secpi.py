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
	if token == TOKEN:
		return render_template('index.html')
	else:
		return render_template('invalid_token.html')


# FRAME GENERATOR #
def gen(camera: Camera) -> any:
	#get camera frame
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
		       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/feed/<token>')
def feed(token) -> Response:
	return Response(gen(pi_camera),
	                mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=DEBUG)
