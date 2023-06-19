def calc(A, B, N):
    max = 0
    for x in range(0, N+1):
        val = A*x//B - A*(x//B)
        if max < val:
            max = val
    return max
