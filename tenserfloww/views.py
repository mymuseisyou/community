import os
import cv2
from PIL import Image
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name

def index(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        _image = fss.save(image.name, image)
        path = os.path.join(settings.MEDIA_ROOT, image.name)

        # Image details
        image_url = fss.url(_image)

        # Read the image
        img = cv2.imread(path)
        img_from_ar = Image.fromarray(img, 'RGB')
        resized_image = img_from_ar.resize((180, 180))
        test_image = np.expand_dims(resized_image, axis=0)

        # Load model
        model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR, 'model.h5'))
        result = model.predict(test_image)
        prediction_idx = np.argmax(result)
        labels = ["negative", "positive",]
        prediction = labels[prediction_idx]

        return TemplateResponse(
            request,
            "index.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "index.html",
            {"message": "No Image Selected"},
        )