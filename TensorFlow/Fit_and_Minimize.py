import tensorflow as tf
import numpy as np
from keras.layers import Input, Dense
from keras.models import Model
from keras import backend as K

def loss_func(y_true, y_pred):
        return tf.reduce_mean(y_pred - y_true, axis=1)

if __name__ == '__main__':
    sess = tf.Session()
    K.set_session(sess)

    inputs = Input(shape=(2,))

    dense_1 = Dense(5, activation='relu',kernel_initializer='ones', bias_initializer='zeros')
    dense_2 = Dense(1, activation='relu',kernel_initializer='ones', bias_initializer='zeros')
    outputs = dense_2(dense_1(inputs))

    model = Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer='rmsprop',
                loss=loss_func,
                #metrics=['accuracy'],
                )

    data   = np.random.random(size=(100,2))
    noise  = np.random.normal(0, 0.05, data.shape[0])
    labels = data[:,0]**2+data[:,1]**2+noise
    for _ in range(100):
        model.fit(data, labels)  # 开始训练

    X_values = tf.get_variable("x_value", initializer=tf.constant([[2,2]],dtype=tf.float32))
    out_values = dense_2(dense_1(X_values))
    sess.run(X_values.initializer)

    #for _ in range(1000):
    #    model.fit(data, labels)  # 开始训练
    #    out1 = sess.run([out_values])
    #    print(out1)

    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(out_values, var_list = [ X_values ])
    for _ in range(100):
        sess.run(train_step)
        out1 = sess.run([X_values,out_values])
        print(out1)
