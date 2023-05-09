def solve():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    ans = [0] * (N - 1)
    for i in range(N):
        for j in range(i + 1, N):
            dist = min(j - i, abs(X - i) + 1 + abs(j - Y))
            ans[dist - 1] += 1
    print(*ans, sep='
')
