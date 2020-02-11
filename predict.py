import cv2
import numpy as np


def predict_type(image, model):
    waste_types = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    img = cv2.imread(image)
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    img_tensor = np.array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    res = list(model.predict(img_tensor)[0])
    type = waste_types[res.index(np.max(res))]

    return type
