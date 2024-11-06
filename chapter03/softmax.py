import numpy as np

def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c) #오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y