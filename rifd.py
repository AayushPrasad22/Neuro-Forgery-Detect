import os
import cv2
import numpy as np
from keras.utils import to_categorical
from keras.layers import  MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten, GlobalAveragePooling2D, BatchNormalization, AveragePooling2D, Input, Conv2D, UpSampling2D
from keras.layers import Convolution2D
from keras.models import Sequential, load_model, Model
import pickle
from sklearn.model_selection import train_test_split
from keras.callbacks import ModelCheckpoint
import keras
from sklearn.metrics import accuracy_score
import keras
from PIL import Image


path = "Dataset/4cam_splc"
X = []
Y = []


for root, dirs, directory in os.walk(path):
    for j in range(len(directory)):
        img = cv2.imread(root+"/"+directory[j])
        name = directory[j].replace(".tif", "_edgemask.jpg")
        mask = cv2.imread("Dataset/edgemask/"+name)
        if img is not None and mask is not None:
            img = cv2.resize(img, (256, 256))
            mask = cv2.resize(mask, (256, 256))
            X.append(img)
            Y.append(mask)
            print(str(j))
            

X = np.asarray(X)
Y = np.asarray(Y)

np.save('model/X',X)
np.save('model/Y',Y)

X = np.load('model/X.npy')
Y = np.load('model/Y.npy')

cv2.imshow("aa", X[0]*255)
cv2.imshow("bb", Y[0]*255)
cv2.waitKey(0)

X = X.astype('float32')
X = X/255
Y = Y.astype('float32')
Y = Y/255

indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]

print(X.shape)
print(Y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2) #split dataset into train and test

input_img = Input(shape=(256, 256, 3))
x = Conv2D(64, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(16, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(16, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)
model = Model(input_img, decoded)
model.compile(optimizer='adam', loss='mean_squared_error')
if os.path.exists("model/rifd.hdf5") == False:
    model_check_point = ModelCheckpoint(filepath='model/rifd.hdf5', verbose = 1, save_best_only = True)
    hist = model.fit(X_train, y_train, batch_size = 32, epochs = 50, validation_data=(X_test, y_test), callbacks=[model_check_point], verbose=1)
    f = open('model/rifd.pckl', 'wb')
    pickle.dump(hist.history, f)
    f.close()    
else:
    model.load_weights("model/rifd.hdf5")

test = cv2.imread("testImages/1.png")
test = test.resize(img, (256, 256))
temp = []
temp.append(test)
test = np.asarray(temp)
test = test.astype('float32')
test = test/255
predict = model.predict(test)
predict = predict[0]
cv2.imshow("a", predict)
cv2.imshow("b", predict*255)
cv2.waitKey(0)
