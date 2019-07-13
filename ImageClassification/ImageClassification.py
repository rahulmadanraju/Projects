# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:38:17 2019

@author: rahul
"""

import numpy as np
import os
from sklearn.metrics import confusion_matrix

import seaborn as sn
import tensorflow as tf
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import cv2

#labelling of class names

class_names = ['mountain', 'street', 'glacier', 'buildings', 'sea', 'forest']
class_names_label = {'mountain': 0,'street' : 1, 'glacier' : 2, 'buildings' : 3, 'sea' : 4, 'forest' : 5}
nb_classes = 6

#loading the data
def load_data():
    
    datasets = ['seg_train/seg_train','seg_test/seg_test']
    size = (150,150)
    output = []
    for dataset in datasets:
        directory = "your file path" + dataset
        images = []
        labels = [] 
        for folder in os.listdir(directory):
            curr_label = class_names_label[folder]
            for file in os.listdir(directory + "/" + folder):
                img_path = directory + "/" + folder + "/" + file
                curr_img = cv2.imread(img_path)
                curr_img = cv2.resize(curr_img, size)
                images.append(curr_img)
                labels.append(curr_label)
        images, labels = shuffle(images, labels)     
        images = np.array(images, dtype = 'float32') 
        labels = np.array(labels, dtype = 'int32')   
        
        output.append((images, labels))

    return output

(train_images, train_labels), (test_images, test_labels) = load_data()

print ("Number of training examples: " + str(train_labels.shape[0]))
print ("Number of testing examples: " + str(test_labels.shape[0]))
print ("Each image is of size: " + str(train_images.shape[1:]))


sizes = np.bincount(train_labels)
explode = (0, 0, 0, 0, 0, 0)  
plt.pie(sizes, explode=explode, labels=class_names,
autopct='%1.1f%%', shadow=True, startangle=150)
plt.axis('equal')
plt.title('Proportion of each observed category')

plt.show()

train_images = train_images / 255.0 
test_images = test_images / 255.0   


fig = plt.figure(figsize=(10,10))
fig.suptitle("Some examples of images of the dataset", fontsize=16)
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (150, 150, 3)), # the nn will learn the good filter to use
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(6, activation=tf.nn.softmax)
])
    


model.compile(optimizer = 'Adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_images, train_labels, batch_size=128, epochs=10, validation_split = 0.2)
    
plt.subplot(211)
plt.plot(history.history['acc'],'bo--', label = "acc")
plt.plot(history.history['val_acc'], 'ro--', label = "val_acc")
plt.title("acc vs val_acc")
plt.legend()

plt.subplot(212)
plt.plot(history.history['loss'],'bo--', label = "loss")
plt.plot(history.history['val_loss'], 'ro--', label = "val_loss")
plt.title("loss vs val_loss")


plt.legend()
plt.show()

test_loss = model.evaluate(test_images, test_labels)

#chossing the random index for the image
index = np.random.randint(test_images.shape[0]) 
img = (np.expand_dims(test_images[index], 0))

# Vector of probabilities
predictions = model.predict(img)   

# We take the highest probability  
pred_img = np.argmax(predictions[0]) 
pred_label = class_names[pred_img]
true_label = class_names[test_labels[index]] 

#Predicted output of the image vs actual output of the image
title = 'Guess : {} VS Pred : {}  '.format(pred_label , true_label )

plt.figure()
plt.imshow(test_images[index])
plt.grid(False)
plt.title(title)
plt.show()

predictions = model.predict(test_images)
pred_labels = np.argmax(predictions, axis = 1)
 
    
    
