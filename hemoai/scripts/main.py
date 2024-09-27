# %%
import numpy as np
import click
from keras.models import load_model
from PIL import Image, ImageOps

np.set_printoptions(suppress=True)

@click.command()
@click.option('--model-path', default='model/keras_model.h5', help='Path to the Keras model file.')
@click.option('--image-path', help='Patdh to the image to classify.', required=True)
@click.option('--labels-path', default='model/labels.txt', help='Path to the labels file.')
def main(model_path, image_path, labels_path):
    model = load_model(model_path, compile=False)

    with open(labels_path, 'r') as f:
        class_names = f.readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    print("Class:", class_name)
    print("Confidence Score:", confidence_score)

if __name__ == '__main__':
    main()