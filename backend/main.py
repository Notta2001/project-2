from sanic import Sanic
import aiofiles
from sanic import response
import numpy as np
import cv2
from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt

physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)


app = Sanic("Upload_Image")

@app.route("/upload", methods=['POST'])
async def omo(request):
    async with aiofiles.open("./images/originalImage.png", 'wb') as f:
        await f.write(request.files["sampleFile"][0].body)
    f.close()
    res50Unet = keras.models.load_model("/home/notta/Desktop/Coding/hust-20212/project2/backend/model/save_model/model-resnet-50-unet.h5")
    img = tf.io.read_file("/home/notta/Desktop/Coding/hust-20212/project2/backend/images/originalImage.png")
    img = tf.image.decode_jpeg(img)

    img  = tf.image.resize(img, (256, 256))
    img = tf.expand_dims(img, axis=0)
    input_image  = tf.cast(img, tf.float32)
    output = res50Unet(tf.convert_to_tensor(input_image/255.0), training=True)
    output_image = np.array(output)
    plt.imshow(output_image[0])
    plt.show()
    return response.json(True)

@app.route("/get_original_img", methods=['GET'])
async def get_original_img(request):
    return await response.file("./images/originalImage.png")

app.run(host='127.0.0.1', port=1337, access_log=False)