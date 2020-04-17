import tensorflow as tf 
from twilio.rest import Client
from pygame import mixer
import geocoder
import numpy as np
from keras.preprocessing import image
import cv2
import os
import time

classifierLoad = tf.keras.models.load_model('Weight_model.h5')

account_sid = 'ACac30b8dc9508af7da4584df94453e6a8'
auth_token = '3b85609972c0267eaaf2e4338a150a0a'


    

def alarm():
    mixer.init()
    sound = mixer.Sound('alarm.wav')
    sound.play()

def send_text_alert():
    message_body ='Health Emergency Current latlong:'
    g = geocoder.ip('me')
    latlong = g.latlng
    lat = latlong[0]
    long = latlong[1]
    #print(latlong)
    message_body = message_body + str(float(lat))+',' + str(float(long))
    print(message_body)
    sms_client = Client(account_sid,auth_token)
    sms_client.messages.create(to="+12488329144",from_="+17244267586",body= message_body)

def send_voice_alert():
    voice_client = Client(account_sid, auth_token)
    voice_client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                               to='+12488329144',
                               from_='+17244267586'
                               )
    

cap= cv2.VideoCapture(0)

if cap.isOpened():
        #print("camera opened")
    ret, frame = cap.read()
    frame = cv2.imwrite('image'+'.jpg',frame)
       # cv2.imshow('frame',frame)
        #print("image created")
    test_image = image.load_img('New_dataset/Drowsiness/Drowsiness652.jpg', target_size = (200,200))
    #test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifierLoad.predict(test_image)
    if result[0][1] == 1:
        print("Heartattack")
    elif result[0][0] == 1:
        print("Drowsiness")
        #send_text_alert()
        #alarm()
    elif result[0][2] == 1:
        print("No_Gesture")
    elif result[0][3] == 1:
        print("Palm_Gesture")
        #send_text_alert()
            #send_voice_alert()
    elif result[0][4] == 1:
        print("Victory_Geture")
    time.sleep(0.5)
    os.remove('image.jpg')
        #print("image deleted")
cap.release()