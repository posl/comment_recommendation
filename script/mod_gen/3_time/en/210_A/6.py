def solve():
    N, A, X, Y = map(int, input().split())
    return min(N, A) * X + max(N - A, 0) * Y
print(solve())
