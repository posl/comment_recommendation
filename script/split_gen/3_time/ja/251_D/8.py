def solve(W):
    N = 300
    A = [0] * N
    A[0] = 1
    A[1] = 2
    A[2] = 3
    if W <= 3:
        return A[0:W]
    else:
        for i in range(3, N):
            A[i] = A[i - 1] + A[i - 2] + A[i - 3]
            if A[i] > W:
                return A[0:i]
        return A[0:N]
