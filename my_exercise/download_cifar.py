from keras.datasets import cifar10
from PIL import Image
import numpy as np
import os

(x_train, y_train), (x_test, y_tdest) = cifar10.load_data()

max_train_num_datas = 500
max_test_num_datas = 100
num_classes = 5
num_datas_list = np.zeros(num_classes)

img_train_dir = "trainData"
img_test_dir = "testData"
id = 0

for x, y in zip(x_train, y_train):

    if np.sum(num_datas_list) > max_train_num_datas * len(num_datas_list):
        break

    label = y[0]
    if label >= num_classes:
        continue

    if num_datas_list[label] == max_train_num_datas:
        continue

    num_datas_list[label] += 1

    img_path = os.path.join(img_train_dir, "{}_{}.jpg".format(label, id))
    id += 1
    img = Image.fromarray(x)
    img.save(img_path)

num_datas_list = np.zeros(num_classes)
for x, y in zip(x_test, y_tdest):

    if np.sum(num_datas_list) > max_test_num_datas * len(num_datas_list):
        break

    label = y[0]
    if label >= num_classes:
        continue

    if num_datas_list[label] == max_test_num_datas:
        continue

    num_datas_list[label] += 1

    img_path = os.path.join(img_test_dir, "{}_{}.jpg".format(label, id))
    id += 1
    img = Image.fromarray(x)
    img.save(img_path)

