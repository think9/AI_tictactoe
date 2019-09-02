import numpy as np
import tensorflow as tf
import pickle

###Data Handling###

#read data from csv file
data_all = np.genfromtxt('data.csv', delimiter=',', dtype=np.float32)
np.random.shuffle(data_all)

#Separate data by 7:3 rate
train_num = int(len(data_all)*0.7)
print(train_num)
test_num = len(data_all)-train_num
data_train = data_all[:train_num]
data_test = data_all[train_num:]
x_train = data_train[:, 0:-1]
y_train = data_train[:, [-1]]
x_test = data_test[:, 0:-1]
y_test = data_test[:, [-1]]

###Train data###
NUM_ITER = 1000
NUM_HIDDEN = 27

X = tf.placeholder(tf.float32, [None, 9])
Y = tf.placeholder(tf.float32, [None, 1])
"""단층 네트워크
W = tf.Variable(tf.random_normal([9, 1]))
B = tf.Variable(tf.random_normal([1]))

H = tf.matmul(X, W) + B
"""

#MLP
W = tf.Variable(tf.random_uniform([9,NUM_HIDDEN], -0.5, 0.5))
B = tf.Variable(tf.random_uniform([1,NUM_HIDDEN], -0.5, 0.5))

#hiddenLayer = tf.sigmoid(tf.matmul(X, W)+B)
hiddenLayer = tf.matmul(X, W)+B
hiddenLayer = tf.sigmoid(hiddenLayer)

W2 = tf.Variable(tf.random_uniform([NUM_HIDDEN,1], -0.5, 0.5))
B2 = tf.Variable(tf.random_uniform([1], -0.5, 0.5))
H = tf.matmul(hiddenLayer, W2)+B2
#outLayer = tf.matmul(hiddenLayer, W2)+B2
#H = tf.sigmoid(outLayer)

cost = tf.reduce_mean(tf.square(H-Y))
optimizer = tf.train.AdamOptimizer(3e-1)
train = optimizer.minimize(cost)

cost_list = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(NUM_ITER):
        sess.run(train, feed_dict={X: x_train, Y: y_train})
        w_pred = sess.run(W).tolist()
        b_pred = sess.run(B).tolist()[0]
        w_pred2 = sess.run(W2).tolist()
        b_pred2 = sess.run(B2).tolist()[0]
        # 1회학습마다 업데이트 된 파라메타 출력
        print(step, w_pred, b_pred, w_pred2, b_pred2)

    print("Test the data")
    true_num = 0
    false_num = 0
    for i in range(0, test_num):
        result = sess.run(H, feed_dict={X: [x_test[i]]})
        #print(y_test[i], result)

        if(result>=0):
            result = 10
        else:
            result = -10
        if result == y_test[i]:
            true_num = true_num + 1
        else:
            false_num = false_num + 1

#Save the parameters
W_list = w_pred
W2_list = w_pred2
B_list = b_pred
B2_list = b_pred2


with open("W_param.pkl", 'wb') as f:
    pickle.dump(W_list, f)

with open("W2_param.pkl", 'wb') as f:
    pickle.dump(W2_list, f)

with open("B_param.pkl", 'wb') as f:
    pickle.dump(B_list, f)

with open("B2_param.pkl", 'wb') as f:
    pickle.dump(B2_list, f)

print(true_num, false_num)