def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M + 1):
        for j in range(min(i, N + 1)):
            B[i - j] += A[N - j] * C[i]
    print(*B)
