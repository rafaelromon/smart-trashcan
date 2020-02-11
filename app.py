#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import tensorflow as tf
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_opencv import Camera

path_model = os.path.join('model.h5')
model = tf.keras.models.load_model(path_model, compile=False)
GPIO_TRIGGER = 13
GPIO_ECHO = 6

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


def init_distance():
    global GPIO_ECHO
    global GPIO_TRIGGER
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_distance():
    global GPIO_ECHO
    global GPIO_TRIGGER
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    if distance > 400: distance=400.0
    return distance


def detect_garbage():
    init_distance()
    total = 0
    errors = 0
    for i in range(5):
        current = get_distance()
        if current >= 400:
            errors+=1
            i-=1
            if errors>5: break
        else:
            total+=current
        time.sleep(0.5)
    avg_distance = total/i+1
    return avg_distance<50

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/classify')
def classify():
    frame = Camera().get_frame()

    waste_types = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    img = cv2.imread(frame)
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    img_tensor = np.array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    res = list(model.predict(img_tensor)[0])
    type = waste_types[res.index(np.max(res))]

    print(type)

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
