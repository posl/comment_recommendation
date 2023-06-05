def solve(N, S):
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i - 1]
    return A
