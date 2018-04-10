"""
Python-28일차(2018.4.10)
"""

## Perceptron 함수
    # 각 논리연산자처럼 결과값이 나올수 있도록 가중치와 임계값을 정의
    
def Perceptron(x1,x2,logic):
    if logic.upper() == 'AND':
        if x1+x2 <= 1:  # w1 = w2 = theta = 1
            return 0
        else:
            return 1
    elif logic.upper() == 'NAND':
        if -x1-x2 <= -2:  # w1 = w2 = -1, theta = -2
            return 0
        else:
            return 1
    elif logic.upper() == 'OR':
        if x1+x2 <= 1/2:  # w1 = w2 = 1, theta = 1/2
            return 0
        else:
            return 1

for i in [0,1]:
    for j in [0,1]:
        print(i,j,Perceptron(i,j,'nand'))


# AND gate
# : 컴퓨터는 두가지의 디지털 값인 0,1을 입력해 하나의 값을 출력하는 회로가 모여 만들어지는데 이 회로를 gate라고 한다.

def AND(x1,x2):
    w1 = 0.7
    w2 = 0.7
    theta = 0.72
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('AND('+str(i)+','+str(j)+') =',AND(i,j))


def NAND(x1,x2):
    w1 = -0.7
    w2 = -0.7
    theta = -0.72
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('NAND('+str(i)+','+str(j)+') =',NAND(i,j))


def OR(x1,x2):
    w1 = 0.7
    w2 = 0.7
    theta = 0.5
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('OR('+str(i)+','+str(j)+') =',OR(i,j))


# 추후에는 가중치, 임계값을 조종한다


## Bias
#  : 퍼셉트론은 입력신호에 가중치를 곱한값과 편향(bias)을 합하여 그 값이 0을 넘으면 1을 출력하고 그렇지 않으면 0을 출력한다.
#    y = wx+b

def AND(x1,x2):
    w1 = 0.7
    w2 = 0.7
    b = -0.72
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('AND('+str(i)+','+str(j)+') =',AND(i,j))


def NAND(x1,x2):
    w1 = -0.7
    w2 = -0.7
    b = 0.72
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('NAND('+str(i)+','+str(j)+') =',NAND(i,j))


def OR(x1,x2):
    w1 = 0.7
    w2 = 0.7
    b = -0.5
    tmp = w1 * x1 + w2 * x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 실행
for i in [0,1]:
    for j in [0,1]:
        print('OR('+str(i)+','+str(j)+') =',OR(i,j))


import numpy as np

x = np.array([0,1])  # input
x

w = np.array([.5,.5])  # weight
w

b = -0.7  # bias

sum(w * x) + b
np.sum(w * x) + b


def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.7,0.7])
    b = -0.72
    tmp = np.sum(w * x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 실행  
for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('AND('+str(i)+','+str(j)+') =',AND(i,j))


def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.7,-0.7])
    b = 0.72
    tmp = np.sum(w * x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 실행  
for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('NAND('+str(i)+','+str(j)+') =',NAND(i,j))


def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.7,0.7])
    b = -0.5
    tmp = np.sum(w * x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

# 실행  
for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('OR('+str(i)+','+str(j)+') =',OR(i,j))



# XOR : eXclusive OR 배타적논리합
# 같으면 0 다르면 1, 한쪽만 1일때만 1을 출력함

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    return AND(s1,s2)

for i,j in ([0,0],[0,1],[1,0],[1,1]):
    print('XOR('+str(i)+','+str(j)+') =',XOR(i,j))


# 퍼셉트론(단층퍼셉트론)은 직선 하나로 나눈 영역만 표현할 수 있다는 한계가 있다.
#  - 선형 : 직선의 영역을 선형영역
#  - 비선형 : 곡선의 영역을 비선형영역
# 다층퍼셉트론으로 비선형 분류를 할 수 있다.
# XOR 단층 퍼셉트론으로 비선형 분류를 할 수 없다. 해결방법은 XOR = (NAND) AND (OR) 조합으로
# 층을 쌓으면 XOR게이트를 구현할 수 있다.


# Step Function

def step_func(x):
    if x > 0:
        return 1
    else:
        return 0

step_func(1)
step_func(-1)
step_func(np.array([1.0,2.0]))  # array로 들어온다면 어떻게 넣어서 처리하지?

# [해결방법]
x = np.array([-1.0,1.0,2.0])
y = x > 0

# bool -> int(True -> 1, False -> 0)
y = y.astype(np.int)  # 자료형 변환
y


def step_func(x):  # 이렇게 해결(이게 for문 안 사용하고 작성해서 좋다)
    y = x > 0
    return y.astype(np.int)

step_func(np.array([-1.0,1.0,2.0]))



# Sigmoid Function
























