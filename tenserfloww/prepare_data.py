import os
import cv2
from PIL import Image
import numpy as np

data = []
labels = []

# Define the labels
label_dict = {
    "negative": 0,
    "positive": 1,
}

for label, idx in label_dict.items():
    image_dir = os.path.join("data", label)
    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)
        image = cv2.imread(image_path)
        image = cv2.resize(image, (180, 180))
        data.append(image)
        labels.append(idx)

data = np.array(data)
labels = np.array(labels)

np.save("chestXray.npy", data)
np.save("labels.npy", labels)

