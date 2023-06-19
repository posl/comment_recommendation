def solve():
    N, W = map(int, input().split())
    events = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    now = 0
    for t, p in events:
        now += p
        if now > W:
            return "No"
    return "Yes"
print(solve())
