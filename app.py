#!/usr/bin/env python
import os
from datetime import datetime
from importlib import import_module

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.backend import set_session

from flask import Flask, render_template, Response, request

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_opencv import Camera

base_path = os.path.dirname(os.path.realpath(__file__))  # This fixes some filepath errors in RPi3

sess = tf.Session()
graph = tf.get_default_graph()

set_session(sess)
model = tf.keras.models.load_model(base_path + "/models/improved_model.h5", compile=False)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Video streaming home page."""

    if request.method == "POST":
        weight = request.form['weight']
        garbage_type = request.form['type']

        json_data = [{
            "measurement": "trash",
            "time": datetime.now(),
            "tags": {
                "garbage_type": garbage_type
            },
            "fields": {
                "weight": weight
            }
        }]

        print(json_data)

    return render_template('index.html')


@app.route('/classify')
def classify():

    global sess
    global graph

    waste_types = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

    frame = Camera().get_frame()
    nparr = np.fromstring(frame, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img = cv2.resize(img_np, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    img_tensor = np.array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    
    with graph.as_default():
        set_session(sess)
        result = list(model.predict(img_tensor)[0])

    type = waste_types[result.index(np.max(result))]

    return type


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
