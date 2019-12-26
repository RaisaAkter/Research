'''
Author: Raisa
Date: 15-12-19
This python script for network architecture
'''
import keras, os
from keras.layers import (Dense, Activation, 
                    Flatten, Conv2D, MaxPooling2D, Dropout)
from keras.models import Sequential, load_model

from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import BatchNormalization
import config


#model_checkpoint_dir = os.path.join(config.checkpoint_path(), "baseline.h5")
model_checkpoint_dir=os.path.join(config.project_root+"checkpoint/","baseline.h5")
#saved_model_dir = os.path.join(config.output_path(), "baseline.h5")
saved_model_dir=os.path.join(config.project_root+"output/","baseline.h5")
print(model_checkpoint_dir,saved_model_dir)

#CNN model
def get_model():
    model = Sequential()
    '''model.add(Conv2D(32, kernel_size=(5,5),input_shape=config.img_shape,padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(64, kernel_size=(3, 3),input_shape=config.img_shape,padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(128,kernel_regularizer=keras.regularizers.l2(l=0.01)))
    model.add(Activation('relu'))
    model.add(Dense(config.num_classes, activation='softmax'))'''
    model.add(Conv2D(32, kernel_size=(5, 5),input_shape=config.img_shape,padding='same'))
    model.add(Activation('relu'))
    model.add(BatchNormalization())

    model.add(Conv2D(32, kernel_size=(3, 3),input_shape=config.img_shape,padding='same'))
    model.add(Activation('relu'))
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2,2)))
    #model.add(Dropout(rate=0.20))

    model.add(Conv2D(64, kernel_size=(3, 3),input_shape=config.img_shape,padding='same'))
    model.add(Activation('relu'))
    model.add(BatchNormalization())

    model.add(Conv2D(64, kernel_size=(3, 3),input_shape=config.img_shape,padding='same'))
    model.add(Activation('relu'))
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2,2)))
    #model.add(Dropout(rate=0.20))

    model.add(Flatten())
    model.add(Dense(128,kernel_regularizer=keras.regularizers.l2(l=0.001)))
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    #model.add(Dropout(rate=0.30))
    model.add(Dense(config.num_classes, activation='softmax'))

    return model


def read_model():
    model = load_model(saved_model_dir)
    return model

def save_model_checkpoint():
    return ModelCheckpoint(model_checkpoint_dir, 
                            monitor = 'val_loss', 
                            verbose = 2, 
                            save_best_only = True, 
                            save_weights_only = False, 
                            mode='auto', 
                            period = 1)

def set_early_stopping():
    return EarlyStopping(monitor = 'val_loss', 
                        patience = 30, 
                        verbose = 2, 
                        mode = 'auto')

if __name__ == "__main__":
    m = get_model()
    m.summary()
print("done")
