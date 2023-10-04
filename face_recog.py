import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
import os
import numpy
import cv2

PATH = "./dataset"
train_images = []
train_labels = []
test_images = []
test_labels = []
for folder in os.listdir(PATH):
    if folder == "Humans":
        label = 0
    else:
        label = 1
    folder_len = len(os.listdir(f"{PATH}/{folder}"))
    for (idx, img) in enumerate(os.listdir(f"{PATH}/{folder}")):
        if img == ".DS_Store":
            continue
        print(f"Processing {folder}/{img}")
        image = cv2.imread(f"{PATH}/{folder}/{img}")
        image = cv2.resize(image, (100, 100))
        if idx < folder_len * 0.8:
            train_images.append(image)
            train_labels.append(label)
        else:
            test_images.append(image)
            test_labels.append(label)

train_images = numpy.array(train_images)
train_labels = numpy.array(train_labels)
test_images = numpy.array(test_images)
test_labels = numpy.array(test_labels)

for folder in os.listdir(PATH):
    if folder == "Humans":
        label = 0
    elif folder == ".DS_Store":
        continue
    else:
        label = 1
    folder_len = len(os.listdir(f"{PATH}/{folder}"))
    for (idx, img) in enumerate(os.listdir(f"{PATH}/{folder}")):
        if img == ".DS_Store":
            continue
        print(f"Processing {folder}/{img}")
        image = cv2.imread(f"{PATH}/{folder}/{img}")
        image = cv2.resize(image, (100, 100))
        if idx < folder_len * 0.8:
            train_images.append(image)
            train_labels.append(label)
        else:
            test_images.append(image)
            test_labels.append(label)

import random
for i in range(len(train_images)):
    rand = random.randint(0, len(train_images) - 1)
    train_images[i], train_images[rand] = train_images[rand], train_images[i]
    train_labels[i], train_labels[rand] = train_labels[rand], train_labels[i]

train_images = numpy.array(train_images)
train_labels = numpy.array(train_labels)
test_images = numpy.array(test_images)
test_labels = numpy.array(test_labels)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels[..., None], epochs=10, 
                    validation_data=(test_images, test_labels[..., None]),
                    callbacks=[tf.keras.callbacks.TensorBoard(log_dir='./logs', update_freq='batch')])

import seaborn as sns
from sklearn.metrics import confusion_matrix
predictions = model.predict(test_images)
predictions = numpy.round(predictions)
cm = confusion_matrix(test_labels, predictions)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()

model.save("./models/face_rec.h5")