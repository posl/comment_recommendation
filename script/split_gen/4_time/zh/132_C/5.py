def solve(N, D):
    D.sort()
    mid = N // 2
    return D[mid] - D[mid-1]
