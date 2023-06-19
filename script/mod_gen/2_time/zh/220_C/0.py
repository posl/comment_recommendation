def sumB(A, N, X):
    B = A * 100
    k = 0
    sumB = 0
    while sumB <= X:
        sumB += B[k]
        k += 1
    return k

if __name__ == '__main__':
    sumB()