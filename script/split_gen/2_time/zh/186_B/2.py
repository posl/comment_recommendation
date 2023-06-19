def solve(H, W, A):
    min = 1000
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    res = 0
    for i in range(H):
        for j in range(W):
            res += A[i][j] - min
    return res
