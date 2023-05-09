def main():
    N, C = map(int, input().split())
    events = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        events.append((a, c))
        events.append((b + 1, -c))
    events.sort()
    ans = 0
    current = 0
    for i in range(len(events) - 1):
        current += events[i][1]
        ans += min(current, C) * (events[i + 1][0] - events[i][0])
    print(ans)

if __name__ == '__main__':
    main()