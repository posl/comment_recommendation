def solve(N, S):
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[0]
    return A
