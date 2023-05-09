def harvest(N, A):
    result = 0
    for i in range(N):
        if A[i] > 10:
            result += A[i] - 10
    return result
