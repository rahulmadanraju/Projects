---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2 - Object Detection framework Yolo V3
In its latest variant version 3, which they have implemented based on Darknet-53, it has 3 multi-scale detection layers with grid size of 13. 26 & 52.
	
* Your task is to remove the smallest of these three layers (with 52x52 grid) and re-implement the Yolo v3 to include only 2 multi-scale detection layers those of 13 and 26 grid sizes.
	
* For the reference of Yolo v3 you can use following repository on Github. Ref: https://github.com/experiencor/keras-yolo3/
	
* Along with the source code, describe the possible approaches that you will take and also explain your thought process as additional documentation.

# Solution 2 - In order to implement the above task following approach was taken:
				
Taking the references of the given information and sources available, I made a study analysis on the model structure.
				
Yolo v3 is the thrid version of Yolo as an object detection model which is considered to give better accuracy on detection. The model consists of 5 residual layers and three multi-scale detection layers with the grid size of:
	
* 13x13 - for detecting large objects
	
* 26x26 - for detecting medium objects
	
* 52x52 - for detecting small objects
					
As per the task assigned, the smallest of the layers are to be removed i.e. 52x52 and re-implement the model including 2 multi-scale detection
We know the model architecture contains 106 layers in which 75 are convolutional layers and remaining consists of shortcut, upsample, yolo and route layers.
Therefore to understand more on the architecture of the V3 model and know the presence of layers in the model, I made use of the code yolo_model.py along with yolo-weights which is attached to this folder and the following were observed and proposed:
* The layers from 1-3: 208x208, 5-10: 104x104, 12-35: 52x52, 37-60: 26x26, 62-84: 13x13 followed by 26  and 52 through upsample by 2 at 85 and 97 layer for Yolo. 
	
Knowing the presence of layers in the model, the following approach was made
* Firstly, the layers from 12-35 was removed/commented which had consisting of 52x52 resulting to a custom model
* The transition of convolution from input 104x104 to output 26x26 had to be performed.

	a. Therefore, the values of stride and kernel has to be determined to bring down the size of the input
	b. On calculating and re-verifying, the stride = 4 and kernel = 5 was used to downsample the input and at the same time make a fair trade to detect small-ranged-medium objects too.(if only two scale detection layers are used)
	
	c. Now there is a downsample from 104x104 to 26x26 in the network and continues further till the yolo layer-94
* We also see that, the model contains 3 detection layers of which the third detection layer at 99 to 106 is not useful without the 52x52 layer. Also, since we have been asked to implement the model for only 2 detection layers, we can elimiate/comment the third detection layer in the model.
	"or"
	d. if needed, we can upsample the 97th layer by 4 to make a transition from 26x26 to 104x104 and use the third detection model for very small object detection.
* Run the custom model again along with yolov3-weights and check for errors
* Made sure the code is working and error free and model weights are being saved to the directory.
					   			
				
---------------------------------------------------------------------------------------------------------------------------------------------------------------
		
References used: 
a. Experiencor - https://github.com/experiencor/keras-yolo3/ 
b. Darknet-53 - https://pjreddie.com/darknet/yolo/
c. MDPI - https://www.mdpi.com/2072-4292/12/1/44/htm
d. Machine Learning Mastery - https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/
e. Cyberailab - https://www.cyberailab.com/post/a-closer-look-at-yolov3
f. Paperspace : Ayoosh - https://blog.paperspace.com/tag/series-yolo/ and https://github.com/ayooshkathuria/pytorch-yolo-v3



Images used: 
a. Structure of the Darknet53 convolutional network - https://www.mdpi.com/2072-4292/12/1/44/htm
