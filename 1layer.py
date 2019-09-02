import numpy as np
import tensorflow as tf
import pickle

###Data Handling###

#read data from csv file
data_all = np.genfromtxt('data.csv', delimiter=',', dtype=np.float32)
np.random.shuffle(data_all)

#Separate data by 7:3 rate
train_num = int(len(data_all)*0.7)
test_num = len(data_all)-train_num
data_train = data_all[:train_num]
data_test = data_all[train_num:]
x_train = data_train[:, 0:-1]
y_train = data_train[:, [-1]]
x_test = data_test[:, 0:-1]
y_test = data_test[:, [-1]]

###Train data###
NUM_ITER = 1000
NUM_HIDDEN = 1

X = tf.placeholder(tf.float32, [None, 9])
Y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_uniform([9,NUM_HIDDEN], -0.5, 0.5))
B = tf.Variable(tf.random_uniform([1,NUM_HIDDEN], -0.5, 0.5))

#hiddenLayer = tf.sigmoid(tf.matmul(X, W)+B)
H = tf.matmul(X, W)+B

cost = tf.reduce_mean(tf.square(H-Y))
optimizer = tf.train.AdamOptimizer(1e-1)
train = optimizer.minimize(cost)

cost_list = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(NUM_ITER):
        sess.run(train, feed_dict={X: x_train, Y: y_train})
        w_pred = sess.run(W).tolist()
        b_pred = sess.run(B).tolist()[0]

        # 1회학습마다 업데이트 된 파라메타 출력
        print(step, w_pred, b_pred)

    print("Test the data")
    true_num = 0
    false_num = 0
    for i in range(0, test_num):
        result = sess.run(H, feed_dict={X: [x_test[i]]})

        if(result>=0):
            result = 10
        else:
            result = -10
        if result == y_test[i]:
            true_num = true_num + 1
        else:
            false_num = false_num + 1

print(true_num, false_num)