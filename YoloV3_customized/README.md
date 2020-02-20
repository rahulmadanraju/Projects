---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 2 - Object Detection framework Yolo V3
In its latest variant version 3, which they have implemented based on Darknet-53, it has 3 multi-scale detection layers with a grid size of 13. 26 & 52.
	
* Your task is to remove the smallest of these three layers (with 52x52 grid) and re-implement the Yolo v3 to include only 2 multi-scale detection layers those of 13 and 26 grid sizes.
	
* For the reference of Yolo v3, you can use the following repository on Github. Ref: https://github.com/experiencor/keras-yolo3/
	
* Along with the source code, describe the possible approaches that you will take and also explain your thought process as additional documentation.

# Solution 2 - In order to implement the above task following approach was taken:
				
Taking the references to the given information and sources available, I made a study analysis of the model structure.

## Introduction

Yolo v3 is the third version of Yolo, on simple terms - an object detection model which is considered to give better accuracy on detection. The model consists of five residual layers and three multi-scale detection layers with the grid size of:
	
	* 13x13 - for detecting large objects
	
	* 26x26 - for detecting medium objects
	
	* 52x52 - for detecting small objects
	
## Approach
					
As per the task assigned, the smallest of the layers are to be removed i.e. 52x52 and re-implement the model including 2 multi-scale detection

We know the model architecture contains 106 layers in which 75 are convolutional layers and remaining consists of shortcuts, upsample, yolo and route layers.

<p align="center"> 
<img src="https://github.com/rahulmadanraju/Projects/blob/master/YoloV3_customized/Images_Report/YOLOv3_architecture.png", width="400", height="400" />
<p>

Therefore to understand more on the architecture of the V3 model and know the layers, I made use of the code yolo_model.py along with yolov3-weights which can be downloaded from this link: https://pjreddie.com/media/files/yolov3.weights .

The following points were observed:

* The layers are arranged from 1-3: 208x208, 5-10: 104x104, 12-35: 52x52, 37-60: 26x26, 62-84: 13x13 followed by yolo detection 1, 2 and 3.  
	
Understanding the presence of layers in the model, the following approach was made
* Copy the code from yolo_model.py to a new file called yolov3_custom_model.py for customization of the model 
* The layers from 12-35 (i.e. 24 layers) was removed/commented which had 52x52, resulting in the formation of a custom model
* The skip_layer at 36 can either be deleted or retained based on the requirement of the third detection layer of yolov3 for conactenation (i.e yolo_3)
* The transition of convolution from input 104x104 to output 26x26 had to be performed. (i.e from layer 11 to 37)

	- Therefore, the values of stride and kernel have to be determined to bring down the size of the input
	- On calculating using the formula and re-verifying it, the stride = 4 and kernel = 5 was used to downsample the input
	- (why kernel 5? - make a fair trade to detect small-ranged-medium and also medium objects - if only two scale detection layers are used), we can also go with bigger kernel, but it solely depends on the size of the object to be detected
	- Now there is a downsample from 104x104 to 26x26 in the network and continues further till the yolo_2 detection layer (at layer-94)
	
* We also see that the model contains 3 detection layers of which the third detection layer yolo_3 (at layers - 99 to 106) is not useful without the 52x52 layers. Also, since we have been asked to implement the model for only 2 detection layers, we can eliminate/comment on the third detection layer "or" if needed, we can upsample the 97th layer by 4 to make a transition from 26x26 to 104x104 and use the third detection model for very-small object detection.

* Run the custom model again along with yolov3-weights and check for errors. When the model is error free, the summary is as shown below.

* Made sure the code is working and error-free for two stage detection and model weights are being saved to the directory.

<p align="center"> 
<img src="https://github.com/rahulmadanraju/Projects/blob/master/YoloV3_customized/Images_Report/Image2.png", width="500", height="300" />
<p>


## Conclusion

Here we observe how the v3 model is designed by removing 52x52 layers and implement the same for two multi-scale detection with a grid size of 13 and 26. The model becomes much faster with the removal of layers and preferably used for detecting medium and large sized objects. The following implementation can also be carried on the other grid sizes based on the requirements of object detection. 
					   			
				
----------------------------------------------------------------------------------------------------------------------------------------
		
## References used: 
* Experiencor - https://github.com/experiencor/keras-yolo3/ 
* Darknet-53 - https://pjreddie.com/darknet/yolo/
* MDPI - https://www.mdpi.com/2072-4292/12/1/44/htm
* Machine Learning Mastery - https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/
* Cyberailab - https://www.cyberailab.com/post/a-closer-look-at-yolov3
* Paperspace : Ayoosh - https://blog.paperspace.com/tag/series-yolo/ and https://github.com/ayooshkathuria/pytorch-yolo-v3



## Images used: 
* Structure of the Darknet53 convolutional network - https://www.mdpi.com/2072-4292/12/1/44/htm
