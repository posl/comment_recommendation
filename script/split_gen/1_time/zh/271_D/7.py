def solve(N, S, A):
    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1 == 1:
                sum += A[j][0]
            else:
                sum += A[j][1]
        if sum == S:
            return i
    return -1
