def pay(N, X, A, B):
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum >= X:
        return True
    else:
        return False

if __name__ == '__main__':
    pay()