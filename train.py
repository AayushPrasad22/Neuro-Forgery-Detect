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


path = "Dataset/Live/Ground_truth"
noise_X = []
clean_Y = []


for root, dirs, directory in os.walk(path):
    for j in range(len(directory)):
        img = cv2.imread(root+"/"+directory[j])
        img = cv2.resize(img, (256, 256))
        name = "noisy_"+directory[j]
        noise = cv2.imread("Dataset/Live/Noisy_folder/"+name)
        noise = cv2.resize(noise, (256, 256))
        noise_X.append(noise)
        clean_Y.append(img)
        print(str(j))
            

noise_X = np.asarray(noise_X)
clean_Y = np.asarray(clean_Y)

np.save('model/noise_X',noise_X)
np.save('model/clean_Y',clean_Y)

noise_X = np.load('model/noise_X.npy')
clean_Y = np.load('model/clean_Y.npy')

cv2.imshow("aa", noise_X[0]*255)
cv2.imshow("bb", clean_Y[0]*255)
cv2.waitKey(0)

noise_X = noise_X.astype('float32')
noise_X = noise_X/255
clean_Y = clean_Y.astype('float32')
clean_Y = clean_Y/255

indices = np.arange(noise_X.shape[0])
np.random.shuffle(indices)
noise_X = noise_X[indices]
clean_Y = clean_Y[indices]

print(noise_X.shape)
print(clean_Y.shape)
X_train, X_test, y_train, y_test = train_test_split(noise_X, clean_Y, test_size=0.2) #split dataset into train and test

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
if os.path.exists("model/noise_detect_clean.hdf5") == False:
    model_check_point = ModelCheckpoint(filepath='model/noise_detect_clean.hdf5', verbose = 1, save_best_only = True)
    hist = model.fit(X_train, y_train, batch_size = 64, epochs = 50, validation_data=(X_test, y_test), callbacks=[model_check_point], verbose=1)
    f = open('model/noise_detect_clean.pckl', 'wb')
    pickle.dump(hist.history, f)
    f.close()    
else:
    model.load_weights("model/noise_detect_clean.hdf5")

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
