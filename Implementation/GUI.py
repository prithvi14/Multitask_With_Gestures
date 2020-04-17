# importing the required modules 
import cv2 
import time

# capturing from the first camera attached 
cap = cv2.VideoCapture(0) 

# will continue to capture until 'q' key is pressed 
while True: 
    i =493
    for i in range(i,1000):
        #time.sleep(1)
        ret, frame = cap.read() 
        
        cv2.imshow('frame', frame) 
        print('frameredy')
       
        frame = cv2.imwrite('Real_time_data/Heartattack/image'+ str(i)+'.jpg',frame)
        print('imageCreated')
        time.sleep(1)
    # Program will terminate when 'q' key is pressed 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break


# Releasing all the resources 
cap.release() 
cv2.destroyAllWindows() 
