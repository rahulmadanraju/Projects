import cv2
import time
import numpy as np

## Preparation for writing the ouput video
video_capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')# note the lower case
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
out = cv2.VideoWriter('Project_Invisible.mp4',fourcc , 100, (frame_width,frame_height), True)

time.sleep(3)
background = 0

for k in range(45):
    ret,background = video_capture.read()
background = np.flip(background,axis=1)

while(video_capture.isOpened()):
    ret, image = video_capture.read()
    if not ret:
        break
    image = np.flip(image,axis=1)
    
    # Change to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Create masks with coordinates to detect the color
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])
    mask_all = cv2.inRange(hsv,lower_blue,upper_blue)


    mask_all = cv2.morphologyEx(mask_all, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask_all = cv2.morphologyEx(mask_all, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
 
 
    #Hide the blue part away
    mask2 = cv2.bitwise_not(mask_all)
 
    streamA = cv2.bitwise_and(image,image,mask=mask2)

    #Copy the masked area's original part
    streamB = cv2.bitwise_and(background, background, mask = mask_all)
 
 
    #Write the video in the file specified in the previous block
    output = cv2.addWeighted(streamA,1,streamB,1,0)
    out.write(output)
    cv2.imshow("cloak_trick",output)
    if cv2.waitKey(25) == 13:
        break
    
video_capture.release()
out.release()
cv2.destroyAllWindows()
