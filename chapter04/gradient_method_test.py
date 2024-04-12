import numpy as np


def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성
    
    for idx in range(x.size):
        tmp_val = x[idx]
        
        # f(x+h) 계산
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)
        
        # f(x-h) 계산
        x[idx] = tmp_val - h 
        fxh2 = f(x) 
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원
        
    return grad

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
        
    return x


def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)


init_x = np.array([-3.0, 4.0])
grad_1 = gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)
print(grad_1)

grad_2 = gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100)
print(grad_2)

grad_3 = gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100)
print(grad_3)