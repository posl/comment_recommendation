def solve(N,A,X):
    A.sort()
    B = A * 100
    sum = 0
    i = 0
    while True:
        sum += B[i]
        if sum > X:
            break
        i += 1
    return i + 1
