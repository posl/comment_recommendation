def solve():
    X, Y, N = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i % 3 == 0:
            ans += Y
        else:
            ans += X
    print(ans)
solve()
