import numpy as np

def AND(x):
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.7                  # 편향
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print('AND(0 , 0) = {}'.format(AND(np.array([0, 0])))) # AND(0, 0) -> 0을 출력
print('AND(0 , 1) = {}'.format(AND(np.array([0, 1])))) # AND(0, 1) -> 0을 출력
print('AND(1 , 0) = {}'.format(AND(np.array([1, 0])))) # AND(1, 0) -> 0을 출력
print('AND(1 , 1) = {}'.format(AND(np.array([1, 1])))) # AND(1, 1) -> 1을 출력
print()

def NAND(x):
    w = np.array([-0.5, -0.5])  # 가중치 AND와는 가중치(w와 b)만 다르다
    b = 0.7                  # 편향
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print('NAND(0 , 0) = {}'.format(NAND(np.array([0, 0])))) # NAND(0, 0) -> 1을 출력
print('NAND(0 , 1) = {}'.format(NAND(np.array([0, 1])))) # NAND(0, 1) -> 1을 출력
print('NAND(1 , 0) = {}'.format(NAND(np.array([1, 0])))) # NAND(1, 0) -> 1을 출력
print('NAND(1 , 1) = {}'.format(NAND(np.array([1, 1])))) # NAND(1, 1) -> 0을 출력
print()

def OR(x):
    w = np.array([0.5, 0.5])  # 가중치 AND와는 가중치(w와 b)만 다르다
    b = -0.2                  # 편향
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print('OR(0 , 0) = {}'.format(OR(np.array([0, 0])))) # OR(0, 0) -> 0을 출력
print('OR(0 , 1) = {}'.format(OR(np.array([0, 1])))) # OR(0, 1) -> 1을 출력
print('OR(1 , 0) = {}'.format(OR(np.array([1, 0])))) # OR(1, 0) -> 1을 출력
print('OR(1 , 1) = {}'.format(OR(np.array([1, 1])))) # OR(1, 1) -> 1을 출력
print()

def XOR(x):
    s1 = NAND(x)
    s2 = OR(x)
    y = AND(np.array([s1, s2]))
    return y

print('XOR(0 , 0) = {}'.format(XOR(np.array([0, 0])))) # OR(0, 0) -> 0을 출력
print('XOR(0 , 1) = {}'.format(XOR(np.array([0, 1])))) # OR(0, 1) -> 1을 출력
print('XOR(1 , 0) = {}'.format(XOR(np.array([1, 0])))) # OR(1, 0) -> 1을 출력
print('XOR(1 , 1) = {}'.format(XOR(np.array([1, 1])))) # OR(1, 1) -> 1을 출력
