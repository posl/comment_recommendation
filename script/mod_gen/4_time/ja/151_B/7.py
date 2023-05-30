def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = N*M - sum(A)
    if X > K:
        return -1
    else:
        return max(0, X)
print(solve())
