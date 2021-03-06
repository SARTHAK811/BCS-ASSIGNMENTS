# -*- coding: utf-8 -*-
"""Copy of ML_assignment (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WaneKvDl2uFlFNCpbWwHK0ozwlh5VVEm

## Question 1 : Linear Regression
To check whether you are able to build simple linear regression model from scratch or not.
"""

import numpy as np
import matplotlib.pyplot as plt
 
!wget --no-check-certificate https://github.com/adigup390/datasets/raw/main/X.npy -O X.npy
!wget --no-check-certificate https://github.com/adigup390/datasets/raw/main/y.npy -O y.npy

def load_data_LR():
  # Implement this function to read the dataset using the path declared in path_X and path_y
  # should return the X and y data
  # use np.load() to load the data google it you will get to know how to do it

  path_X = "X.npy"
  path_y = "y.npy"
  X=np.load(X.npy)
  y=np.load(y.npy)

  # Write your code here ----------

  # -------------------------------

  return X, y

def get_linear_model(X, y):
  # This shoudl return a proper linear model without bias of type y = XW

  # Write your code here ----------
  
  # -------------------------------
  D=X.shape[0]
  out_shape=1
  W = np.random.randn(D, out_shape)

  return W

def MSE(y, y_pred):
  # should return the mean square error between the actual y and predicted y

  # Write your code here ----------
  
  # -------------------------------
  count =0
  sum=0
  for a in y:
    sum=sum+(a[0]-(y_pred[count])[0])**2
    count=count+1
  error=sum/count
  return error

def train_by_algebra(X, y):
  # should return the trained weight 'W' using the linear algebra method i.e. setting dE/dW = 0

  # Write your code here ----------
  
  # -------------------------------
  Z=X.transpose()
  U=np.dot(Z,X)
  F= np.linalg.inv(U)
  L=np.dot(F,Z)
  W=np.dot(L,y)
  return W

def train_by_GD(X, y, epochs=5, lr=0.01):
  # should return the trained weight 'W' using the gradient descent for number of iterations equals to epochs
  # should also return error history int the cariable error_hist.shape = (epochs,); error_hist[i] = mean square error after epoch i-1
  # should also print mean square error after each epoch/ iteration
  # lr = "learning rate" i.e. eta
  
  # Write your code here ----------
  
  # -------------------------------
  W=get_linear_model(X,y)
  error_hist[0]=MSE(y,np.dot(X,W))
  print(error_hist[0])
  for i in range(epochs):
    P=np.transpose(-X)
    Q=y-np.dot(X,W)
    G=np.dot(P,Q)
    W=W-lr*G
    y_pred=np.dot(X,W)
    error_hist[i]=MSE(y,y_pred)
    print(error_hist[i])





  return W, error_hist

"""### Now write a complete code using the function defined above to learn the model for following cases:

##### Learn **W** using linear algebra method and prints mean square error between actual y and predicted y. Use `y_pred = XW`. Also plot y_pred and y on different plots.
"""

# Write your code here ----------
  
# -------------------------------
import numpy as np
import matplotlib.pyplot as plt
 


def load_data_LR():
  # Implement this function to read the dataset using the path declared in path_X and path_y
  # should return the X and y data
  # use np.load() to load the data google it you will get to know how to do it

  path_X = "X.npy"
  path_y = "y.npy"
  X=np.load(path_X)
  y=np.load(path_y)



  # Write your code here ----------

  # -------------------------------

  return X, y

def get_linear_model(X, y):
  # This shoudl return a proper linear model without bias of type y = XW

  # Write your code here ----------
  
  # -------------------------------
  D=1
  out_shape=1
  W = np.random.randn(D, out_shape)

  return W

def MSE(y, y_pred):
  # should return the mean square error between the actual y and predicted y

  # Write your code here ----------
  
  # -------------------------------
  count =0
  sum=0
  for a in y:
    sum=sum+(a[0]-(y_pred[count])[0])**2
    count=count+1
  error=sum/count
  return error

def train_by_algebra(X, y):
  # should return the trained weight 'W' using the linear algebra method i.e. setting dE/dW = 0

  # Write your code here ----------
  
  # -------------------------------
  Z=X.transpose()
  U=np.dot(Z,X)
  F= np.linalg.inv(U)
  L=np.dot(F,Z)
  W=np.dot(L,y)
  return W

def train_by_GD(X, y, epochs=5, lr=0.01):
  # should return the trained weight 'W' using the gradient descent for number of iterations equals to epochs
  # should also return error history int the cariable error_hist.shape = (epochs,); error_hist[i] = mean square error after epoch i-1
  # should also print mean square error after each epoch/ iteration
  # lr = "learning rate" i.e. eta
  
  # Write your code here ----------
  
  # -------------------------------
  W=get_linear_model(X,y)
  T=np.dot(X,W)
  error_hist=[]
  error_hist.append(MSE(y,T))
  print(error_hist[0])
  for i in range(epochs):
    P=np.transpose(-X)
    Q=y-np.dot(X,W)
    G=np.dot(P,Q)
    W=W-lr*G
    y_pred=np.dot(X,W)
    error_hist.append(MSE(y,y_pred))
    print(error_hist[i+1])
    




  return W, error_hist

!wget --no-check-certificate https://github.com/adigup390/datasets/raw/main/X.npy -O X.npy
!wget --no-check-certificate https://github.com/adigup390/datasets/raw/main/y.npy -O y.npy
X,y=load_data_LR()
print(X)
print(y)
W= train_by_algebra(X,y)
print(W)
y_pred=np.dot(X,W)
print("Mean Squared Error is:")
print(MSE(y,y_pred))
plt.plot(X,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph of Actual y')
plt.show()
plt.plot(X,y_pred)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph of y predicted')
plt.show()
plt.plot(X,y,label='y actual')
plt.plot(X,y_pred,label='y predicted')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Comaprison between y and y_pred')
plt.legend()
plt.show()

"""##### Learn **W** using gradient descent method for following learning rates, `lr = [0.01, 0.001, 0.0001]` for **10 epochs**. Plot **MSE vs epochs** for each of them.  Also plot y_pred and y on different plots."""

# Write your code here ----------
  
# -------------------------------
import numpy as np
import matplotlib.pyplot as plt
 
def load_data_LR():
  # Implement this function to read the dataset using the path declared in path_X and path_y
  # should return the X and y data
  # use np.load() to load the data google it you will get to know how to do it

  path_X = "X.npy"
  path_y = "y.npy"
  X=np.load(path_X)
  y=np.load(path_y)



  # Write your code here ----------

  # -------------------------------
  return X, y

def get_linear_model(X, y):
  # This shoudl return a proper linear model without bias of type y = XW

  # Write your code here ----------
  
  # -------------------------------
  D=1
  out_shape=1
  W = np.random.randn(D, out_shape)

  return W

def MSE(y, y_pred):
  # should return the mean square error between the actual y and predicted y

  # Write your code here ----------
  
  # -------------------------------
  count =0
  sum=0
  for a in y:
    sum=sum+(a[0]-(y_pred[count])[0])**2
    count=count+1
  error=sum/count
  return error

def train_by_GD(X, y, epochs=5, lr=0.01):
  # should return the trained weight 'W' using the gradient descent for number of iterations equals to epochs
  # should also return error history int the cariable error_hist.shape = (epochs,); error_hist[i] = mean square error after epoch i-1
  # should also print mean square error after each epoch/ iteration
  # lr = "learning rate" i.e. eta
  
  # Write your code here ----------
  
  # -------------------------------
  W=get_linear_model(X,y)
  T=np.dot(X,W)
  error_hist=[]
  error_hist.append(MSE(y,T))
  print(error_hist[0])
  for i in range(epochs):
    P=np.transpose(-X)
    Q=y-np.dot(X,W)
    G=np.dot(P,Q)
    W=W-lr*G
    y_pred=np.dot(X,W)
    error_hist.append(MSE(y,y_pred))
    print(error_hist[i+1])
    
    
  return W, error_hist,y_pred

!wget --no-check-certificate https://github.com/adigup390/datasets/raw/main/X.npy -O X.npy
!wget --no-check-certificate https://github.com/adigup390/datasets/raw/main/y.npy -O y.npy

X,y=load_data_LR()


V,A,y_pred=train_by_GD(X,y,10,0.01)
array=[0,1,2,3,4,5,6,7,8,9,10]
plt.plot(array,A)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('MSE vs epochs')
plt.show()
plt.plot(X,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of y')
plt.show()
plt.plot(X,y_pred)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of y_pred')
plt.show()

V,A,y_pred=train_by_GD(X,y,10,0.001)
array=[0,1,2,3,4,5,6,7,8,9,10]
plt.plot(array,A)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('MSE vs epochs')
plt.show()
plt.plot(X,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of y')
plt.show()
plt.plot(X,y_pred)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of y_pred')
plt.show()

V,A,y_pred=train_by_GD(X,y,10,0.0001)
array=[0,1,2,3,4,5,6,7,8,9,10]
plt.plot(array,A)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('MSE vs epochs')
plt.show()
plt.plot(X,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of y')
plt.show()
plt.plot(X,y_pred)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Plot of y_pred')
plt.show()



"""## Question 2: Image Classification in Tensorflow using Deep Learning
To check whether you are able to build a given neural network model in tensorflow or not. First we will build a fully connected NN model second we will build a CNN model.
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def plot_history(history):
  # function to plot accuracy vs epoch

  plt.plot(history.history['accuracy'], label='accuracy')
  plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(loc='lower right')

def load_data_cifar10_norm():
  # should return the normalised cifar10 dataset by loading it from tensorflow
  # link: https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/

  # Write your code here ----------

  # -------------------------------
  cifar10=tf.keras.datasets.cifar10
  (x_train,y_train),(x_test,y_test)=cifar10.load_data()
  return x_train, y_train, x_test, y_test

"""### Define a fully connected neural network model with following attributes:

*   Total number of **hidden layers = 4**, all with **relu** activation
*   Number of neurons in **first hidden layer = 7200**
*   Number of neurons in **second hidden layer = 2304**
*   Number of neurons in **third hidden layer = 1024**
*   Number of neurons in **fourth hidden layer = 64**

"""

def build_fc_model(input_shape=(32, 32, 3), num_class=10):
  # should return a sequential model defined based on the above attributes
  # do not compile the model

  # Write your code here ----------

  # -------------------------------
  model=tf.keras.models.Sequential(
      [tf.keras.layers.Flatten(input_shape),
       tf.keras.layers.Dense(7200,activation=tf.nn.relu),
       tf.keras.layers.Dense(2304,activation=tf.nn.relu),
       tf.keras.layers.Dense(1024,activation=tf.nn.relu),
       tf.keras.layers.Dense(64,activation=tf.nn.relu),
       tf.keras.layersDense(num_class,activation=tf.nn.softmax)
       ]
  )

  return model

"""### Define a CNN model with following attribute:

*   Total number of **hidden layer = 4**
*   After every convolutional layer there must be a MaxPoolingLayer of size (2, 2)
*   Total number of convolutional layer = 3, all with **relu** activation.
    *    Number of filters in **first convolutional layer = 32**
    *    Number of filters in **second convolutional layer = 64**
    *    Number of filters in **third convolutional layer = 64**
*   After all convolutional layer flatten the output and use **dense layer of 64 neurons**


"""

def build_cnn_model(input_shape=(32, 32, 3), num_class=10):
  # should return a sequential model defined based on the above attributes
  # do not compile the model

  # Write your code here ----------

  # -------------------------------
  model=tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(num_class,activation='softmax'),
  ])

  return model

"""### Compile and train the fully connected neural network model using the above functions."""

# Write your code here ----------

# -------------------------------
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, batch_size=512,
                    validation_data=(x_test, y_test))

plot_history(history)
model.summary()

"""### Compile and train the CNN model using the above functions."""

# Write your code here ----------

# -------------------------------
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, batch_size=512,
                    validation_data=(x_test, y_test))


plot_history(history)
model.summary()

"""### What do you observe? Compare both the model by looking at their Accuracy vs Epoch plot and total numbers of trainable parameters."""

#print("Replace this with your observation")
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def plot_history(history):
  # function to plot accuracy vs epoch

  plt.plot(history.history['accuracy'], label='accuracy')
  plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(loc='lower right')

def load_data_cifar10_norm():
  # should return the normalised cifar10 dataset by loading it from tensorflow
  # link: https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/

  # Write your code here ----------

  # -------------------------------
  cifar10=tf.keras.datasets.cifar10
  (x_train,y_train),(x_test,y_test)=cifar10.load_data()
  return x_train, y_train, x_test, y_test

def build_fc_model(input_shape=(32, 32, 3), num_class=10):
  # should return a sequential model defined based on the above attributes
  # do not compile the model

  # Write your code here ----------

  # -------------------------------
  model=tf.keras.models.Sequential(
      [tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(7200,activation=tf.nn.relu),
       tf.keras.layers.Dense(2304,activation=tf.nn.relu),
       tf.keras.layers.Dense(1024,activation=tf.nn.relu),
       tf.keras.layers.Dense(64,activation=tf.nn.relu),
       tf.keras.layers.Dense(num_class,activation=tf.nn.softmax)
       ]
  )

  return model


x_train,y_train,x_test,y_test=load_data_cifar10_norm()
model=build_fc_model()

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, batch_size=512,
                    validation_data=(x_test, y_test))


plot_history(history)
model.summary()

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def plot_history(history):
  # function to plot accuracy vs epoch

  plt.plot(history.history['accuracy'], label='accuracy')
  plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(loc='lower right')

def load_data_cifar10_norm():
  # should return the normalised cifar10 dataset by loading it from tensorflow
  # link: https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/

  # Write your code here ----------

  # -------------------------------
  cifar10=tf.keras.datasets.cifar10
  (x_train,y_train),(x_test,y_test)=cifar10.load_data()
  return x_train, y_train, x_test, y_test

def build_cnn_model(input_shape=(32, 32, 3), num_class=10):
  # should return a sequential model defined based on the above attributes
  # do not compile the model

  # Write your code here ----------

  # -------------------------------
  model=tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(num_class,activation='softmax'),
  ])

  return model

x_train,y_train,x_test,y_test=load_data_cifar10_norm()
model=build_cnn_model()
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, batch_size=512,
                    validation_data=(x_test, y_test))


plot_history(history)
model.summary()

"""As can be seen in fully connected neural network model , the trainable parameters are less as compared to the convolutionary neural network.
Comparing accuracy and validation accuracy of the model :-
1. In fully connected neural network the accuracy,the overall accuracy and validation accuracy is far smaller as compared to the convolutionary neural network.
2.In convolutionary neural network the validation accuracy and accuracy are close to each other also accuracy approaches to 0.6521 and validation accuracy approaches to 0.6006
3.And also validation accuracy in fully connected neural network is constant that is 0.1

"""