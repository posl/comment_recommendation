def solve():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y
print(solve())
