def main():
    N, C = map(int, input().split())
    events = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        events.append((a-1, c))
        events.append((b, -c))
    events.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in events:
        ans += min(C, fee) * (x - t)
        fee += y
        t = x
    print(ans)

if __name__ == '__main__':
    main()