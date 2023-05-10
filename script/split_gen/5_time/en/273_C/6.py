def solve(N, A):
    B = sorted(A)
    C = [0] * (N + 1)
    for i in range(N):
        if i == 0 or B[i] != B[i-1]:
            C[i+1] = 1
    for i in range(1, N + 1):
        C[i] += C[i-1]
    for i in range(N):
        print(C[B.index(A[i])])
