def solve():
    N, X = map(int, input().split())
    X = X * 100
    count = 0
    for i in range(N):
        v, p = map(int, input().split())
        count += v * p
        if count > X:
            print(i + 1)
            return
    print(-1)
