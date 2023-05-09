def main():
    N, C = map(int, input().split())
    events = []
    for i in range(N):
        a, b, c = map(int, input().split())
        events.append((a, c))
        events.append((b+1, -c))
    events.sort()
    ans = 0
    d = 0
    t = 0
    for event in events:
        if t > 0:
            ans += min(C, t) * (event[0] - d)
        d = event[0]
        t += event[1]
    print(ans)
