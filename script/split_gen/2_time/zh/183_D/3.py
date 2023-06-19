def solve():
    N, W = map(int, input().split())
    events = []
    for i in range(N):
        S, T, P = map(int, input().split())
        events.append((S, P))
        events.append((T, -P))
    events.sort()
    water = 0
    for _, p in events:
        water += p
        if water > W:
            print('No')
            return
    print('Yes')
