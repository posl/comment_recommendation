def main():
    N, C = map(int, input().split())
    events = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        events.append((a, c))
        events.append((b + 1, -c))
    events.sort()
    ans = 0
    cur = 0
    prev = -1
    for day, cost in events:
        if prev >= 0:
            ans += min(C, cur) * (day - prev)
        cur += cost
        prev = day
    print(ans)
