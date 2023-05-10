def check(x):
    sum = 0
    for i in range(0, N):
        sum += C[i] * (A[i][j] for j in range(0, M) if x & (1 << j) > 0)
    if sum >= X:
        return True
    else:
        return False
