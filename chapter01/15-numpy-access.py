import numpy as np

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X.shape)

print(X[0])
print(X[0][1])

for row in X:
    print(row)

X = X.flatten()  # X를 1차원 배열로 변환(평탄화)
print(X)

print(X[np.array([0, 2, 4])]) # 인덱스 0, 2, 4번 원소 얻기

print(X > 15)
print(X[X > 15])
