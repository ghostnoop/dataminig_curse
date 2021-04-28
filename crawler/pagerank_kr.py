import numpy as np


def get_mx():
    with open('matrix.txt', 'r') as f:
        matrix_text = f.read().replace('\"', '').replace('\'', '')

    mx = []
    for i in matrix_text.strip().split('\n'):
        t = []
        for j in i.split(','):
            if '/' in j:
                a, b = j.split('/')
                t.append(float(int(a) / int(b)))
            else:
                t.append(0)
        mx.append(t)
    return mx


n = 5
beta = 0.8
k = (1 - beta) / n

matrix = np.matrix(get_mx())

print('Матрица')
print(matrix)
print()
print()

v_vector = np.matrix([[1 / n] for i in range(n)])
print('вектор')
print(v_vector)
print()
print()

POW = 100
matrix_powed = matrix
for i in range(POW):
    matrix_powed = matrix_powed.dot(matrix)

print('Матрица в степени', POW)
print(matrix_powed)
print()
print()

matrix_final = np.dot(matrix_powed, v_vector)
print('вектор на матрицу')
print(matrix_final)
print()
print()

MATRIX_final_beta = matrix_final.dot(beta)
print('матрица после beta')
print(MATRIX_final_beta)
print()
print()


e = np.matrix([[1.] for i in range(n)])
e = e.dot(k)
print('e')
print(e)
print()
print()

result = MATRIX_final_beta + e

print('результат')
print(result)
print(result.sum())
