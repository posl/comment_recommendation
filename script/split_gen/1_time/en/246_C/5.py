def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = max(A[i] - X * K, 0)
    print(sum(B))
