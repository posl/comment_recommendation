def main():
    N, X, Y = map(int, input().split())
    print((N-1)*X if N < 2 else (N-1) * min(X, Y) + max(0, Y - X))
