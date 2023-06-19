def solve():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    x = x[::-1]
    ans = [i for i in range(N, 0, -1)]
    for i in range(Q):
        ans[x[i]-1], ans[x[i]] = ans[x[i]], ans[x[i]-1]
    print(*ans)
solve()
