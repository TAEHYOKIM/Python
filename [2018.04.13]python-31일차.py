#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python-31일차(2018.4.13)
"""

'''
[문제201] x 변수는 1행 3열 모양의 1,2,3을 입력,
        w 변수는 3행 1열 모양의 2,2,2를 입력,
        y 변수는 x와 w를 행렬의 곱을 이용한 결과를 수행하는 프로그램을 작성하세요.
'''
import numpy as np

x = np.array([[1,2,3]])
x
x.shape

w = np.array([[2],[2],[2]])
w
w.shape

y = np.dot(x,w)
y


import tensorflow as tf
x = np.array([[1,2,3]],dtype='int32')
w = np.array([[2],[2],[2]],dtype='int32')

x = tf.constant(x)
x

w = tf.constant(w)
w

y = tf.matmul(x,w) # int64(array 기본값)은 안되네

sess = tf.Session()
sess.run(x)
sess.run(w)
sess.run(y)
sess.close()

with tf.Session() as sess:
    print(sess.run(y))


x = tf.placeholder(dtype=tf.float32,shape=(1,3))
x

w = tf.placeholder(dtype=tf.float32,shape=(3,1))
w

y = tf.matmul(x,w)

with tf.Session() as sess:
    print(sess.run(y, feed_dict={x:[[1,2,3]],w:[[2],[2],[2]]}))


# 선생님 풀이
import tensorflow as tf

x = tf.constant([[1.0, 2.0, 3.0]])
w = tf.constant([[2.0],[2.0],[2.0]])
y = tf.matmul(x,w)

print(x.get_shape())
print(w.get_shape())
sess = tf.Session()
print(sess.run(x))
print(sess.run(w))
print(sess.run(y))
sess.close()


import tensorflow as tf

x = tf.Variable([[1., 2., 3.]])
w = tf.Variable([[2.],[2.],[2.]])
y = tf.matmul(x, w)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op) # 변수 초기화
    result = sess.run(y)
    print(result)
    



'''
[문제202] (Linear Regression) 학습을 통해서 입력값에 대한 예측값을 출력해주세요.


x(입력)   y(출력)
-------  --------
1	      2
2	      4
3	      6
4	      8
5	      10
6	      12



print(sess.run(hypothesis, feed_dict={X:7}))

[ 13.99977493]


print(sess.run(hypothesis, feed_dict={X:8}))

[ 15.99969196]
'''

import tensorflow as tf
x = tf.constant([1,2,3,4,5,6])
y = tf.constant([2,4,6,8,10,12])



with tf.Session() as sess:
    print(sess.run(x))
















# 선생님 풀이
    
# Linear Regression

import tensorflow as tf

x_data = [1, 2, 3, 4, 5, 6]
y_data = [2, 4, 6, 8, 10, 12]


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1],seed=0), name='weight') # 정규분포 난수
b = tf.Variable(tf.random_normal([1],seed=0), name='bias')


hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y)) # 오차값


optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)


sess = tf.Session()
sess.run(W)

sess.run(tf.global_variables_initializer()) # 변수 초기화


for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],feed_dict={X: x_data, Y: y_data})
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)



print(sess.run(hypothesis, feed_dict={X:7}), cost_val,W_val,b_val)



'''
x1 공부시간  2     4     6     8
x2 학원수   0     4     2     3
y_data 점수    71    93    91    97
'''
data = [[2,0,71],[4,4,93],[6,2,91],[8,3,97]]

x1 = [i[0] for i in data]
x1

x2 = [i[1] for i in data]
x2

y_data = [i[2] for i in data]
y_data


# y = a1 * x1 + a2 * x2 + b

a1 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64,seed=0))
a2 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64,seed=0))
b = tf.Variable(tf.random_uniform([1],0,100,dtype=tf.float64,seed=0))

y = a1 * x1 + a2 * x2 + b  # y는 예측값

rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))  # 오차값

learning_rate = 0.1  # 학습률

gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2000):
        sess.run(gradient_descent)
        w1 = sess.run(a1)
        w2 = sess.run(a2)
        b1 = sess.run(b)
        if step % 100 == 0:
            print(step,sess.run(rmse),sess.run(a1),sess.run(a2),sess.run(b))
          
w1*3+w2*5+b1 # 공부시간 3, 학원 5 인 점수예측


# 추가 연구
data = [[2,0,71],[4,4,93],[6,2,91],[8,3,97]]

x1 = [i[0] for i in data]
x1

x2 = [i[1] for i in data]
x2

y_data = [i[2] for i in data]
y_data


X = tf.placeholder(tf.float32,shape=(2,1))
Y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float32,seed=0))
w2 = tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float32,seed=0))
W = tf.placeholder(tf.float32,shape=(1,2))

b = tf.Variable(tf.random_uniform([1],0,100,dtype=tf.float32,seed=0))

H = tf.matmul()

rmse = 

