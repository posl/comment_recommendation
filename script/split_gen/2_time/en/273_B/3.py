def solve():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 == 0:
            X //= 10
        else:
            X -= 1
    print(X)
solve()
