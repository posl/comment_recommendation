def solve(N, A):
    s = 0
    max_s = 0
    for i in range(N):
        s += A[i]
        if s > max_s:
            max_s = s
    return max_s
