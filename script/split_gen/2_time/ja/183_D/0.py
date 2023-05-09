def main():
    N, W = map(int, input().split())
    events = []
    for _ in range(N):
        S, T, P = map(int, input().split())
        events.append((S, P))
        events.append((T, -P))
    events.sort()
    now = 0
    for _, P in events:
        now += P
        if now > W:
            print('No')
            return
    print('Yes')
