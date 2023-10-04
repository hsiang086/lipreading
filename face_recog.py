import tensorflow as tf
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




