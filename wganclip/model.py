import tensorflow as tf
from tensorflow.keras import layers



# def make_generator_model_mnist():
    
#     model = tf.keras.Sequential()
#     model.add(layers.Reshape((1,1,100),input_shape=(100,)))
#     model.add(layers.Conv2DTranspose(1024, (4, 4), strides=(1, 1),padding = 'valid', use_bias=False))
#     model.add(layers.BatchNormalization())
#     model.add(layers.ReLU())
    

#     model.add(layers.Conv2DTranspose(512, (4, 4), strides=(2, 2),padding = 'same', use_bias=False))
#     model.add(layers.BatchNormalization())
#     model.add(layers.ReLU())


#     model.add(layers.Conv2DTranspose(256, (4,4), strides=(2, 2),padding = 'same', use_bias=False))
#     model.add(layers.BatchNormalization())
#     model.add(layers.ReLU())
    
#     model.add(layers.Conv2DTranspose(1, (4, 4), strides=(2, 2),padding = 'same', use_bias=False,activation='tanh'))

#     return model
def make_generator_model_mnist():
    model = tf.keras.Sequential()
    model.add(layers.Dense(64, use_bias=False, input_shape=(100,), activation='relu'))
    model.add(layers.Dense(512, use_bias=False, activation='relu'))
    model.add(layers.Dense(1152, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.Reshape((3, 3, 128)))
    assert model.output_shape == (None, 3, 3, 128) # Note: None is the batch size

    model.add(layers.Conv2DTranspose(64, (3, 3), strides=(2, 2), use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())

    model.add(layers.Conv2DTranspose(32, (3, 3), strides=(2, 2), padding='valid', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())

    model.add(layers.Conv2DTranspose(1, (4, 4), strides=(2, 2), padding='valid', use_bias=False, activation='tanh'))

    return model


def make_discriminator_model_mnist():

    model = tf.keras.Sequential()
    model.add(layers.Conv2D(256, (4, 4), strides=(2, 2), padding='same',
                                     input_shape=[32, 32, 1]))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(0.2))

    model.add(layers.Conv2D(512, (4, 4), strides=(2, 2), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(0.2))
    
    model.add(layers.Conv2D(1024, (4, 4), strides=(2, 2), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(0.2))

    model.add(layers.Flatten())
    model.add(layers.Dense(1))

    return model



def make_generator_model_svhn():
    model = tf.keras.Sequential()
    model.add(layers.Dense(64, use_bias=False, input_shape=(100,), activation='relu'))
    model.add(layers.Dense(512, use_bias=False, activation='relu'))
    model.add(layers.Dense(1152, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.Reshape((3, 3, 128)))
    assert model.output_shape == (None, 3, 3, 128) # Note: None is the batch size

    model.add(layers.Conv2DTranspose(64, (3, 3), strides=(2, 2), use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())

    model.add(layers.Conv2DTranspose(32, (3, 3), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.ReLU())

    model.add(layers.Conv2DTranspose(1, (3, 3), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    assert model.output_shape == (None, 28, 28, 1)

    return model


def make_discriminator_model_svhn():
    model = tf.keras.Sequential()
    model.add(layers.Conv2D(32, (3, 3), strides=(2, 2), padding='same',
                                     input_shape=[28, 28, 1]))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(64, (3, 3), strides=(2, 2)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128, (3, 3), strides=(2, 2)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))   

    model.add(layers.Flatten())
    model.add(layers.Dense(512, use_bias=False))
    model.add(layers.LeakyReLU())
    model.add(layers.Dense(64, use_bias=False))
    model.add(layers.LeakyReLU())
    model.add(layers.Dense(16, use_bias=False))
    model.add(layers.LeakyReLU())
    model.add(layers.Dense(1))

    return model

