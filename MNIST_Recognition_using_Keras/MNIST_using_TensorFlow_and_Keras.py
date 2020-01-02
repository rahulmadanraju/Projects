import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(xtrain,ytrain), (xtest,ytest) = mnist.load_data()
xtrain = tf.keras.utils.normalize(xtrain, axis=1)
xtest = tf.keras.utils.normalize(xtest, axis=1)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model .compile(optimizer='adam', loss= 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit (xtrain, ytrain, epochs=3)

print(predictions)
print(np.argmax(predictions[0]))

plt.imshow(xtrain[0], cmap = plt.cm.binary)
plt.show()
print (xtrain[0]) 

model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict(xtest)
print (predictions)
print(np.argmax(predictions[0]))


plt.imshow(xtest[0])
plt.show()