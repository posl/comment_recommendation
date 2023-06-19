def solve(A, B, K):
    if K <= A:
        return (A - K, B)
    else:
        return (0, B - (K - A))
A, B, K = map(int, input().split())
print(*solve(A, B, K))
