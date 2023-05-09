def main():
    N, C = map(int, input().split())
    events = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        events.append((a, c))
        events.append((b+1, -c))
    events.sort()
    total = 0
    prev = 0
    ans = 0
    for day, cost in events:
        ans += min(C, total) * (day - prev)
        total += cost
        prev = day
    print(ans)

if __name__ == '__main__':
    main()