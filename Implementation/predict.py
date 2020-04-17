# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(200, 200))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 200, 200, 3)
    # center pixel data
    #img = img.astype('float32')
    #img = img - [123.68, 116.779, 103.939]
    return img

# load an image and predict the class
def run_example():
    # load the image
    img = load_image('Sample_Images/WIN_20200327_14_07_24_Pro.jpg')
    # load model
    model = load_model('Weight_model.h5')
    # predict the class
    result = model.predict(img)
    if result[0][1] == 1:
        print("Heartattack")
    elif result[0][0] == 1:
        print("Drowsiness")
    elif result[0][2] == 1:
        print("No_Gesture")
    elif result[0][3] == 1:
        print("Plam_Gesture")
    elif result[0][4] == 1:
        print("Victory_Gesture")
# entry point, run the example
run_example()