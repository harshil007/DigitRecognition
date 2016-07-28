from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from keras.models import model_from_json
from PIL import Image

import scipy.misc as smp
import numpy as np
import resize


model = model_from_json(open('my_model_architecture.json').read())
model.load_weights('my_model_weights.h5')

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

image_path = input("Enter image path: ")
converted = resize(image_path)

ima = Image.open(converted)
pixels = np.array(ima.getdata())


width, height = ima.size
#pixels = np.array(pixels)
pixels = pixels.reshape(1, 784)


ans = model.predict(x=pixels)
print("\n\n", ans)
