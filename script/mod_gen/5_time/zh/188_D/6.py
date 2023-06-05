def solve():
    N, C = map(int, input().split())
    events = []
    for i in range(N):
        a, b, c = map(int, input().split())
        events.append((a, c))
        events.append((b+1, -c))
    events.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in events:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)
solve()
