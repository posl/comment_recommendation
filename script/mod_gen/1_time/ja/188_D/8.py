def main():
    N, C = map(int, input().split())
    #print(N, C)
    events = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        #print(a, b, c)
        events.append((a, c))
        events.append((b+1, -c))
    #print(events)
    events.sort()
    #print(events)
    ans = 0
    t = 0
    for day, cost in events:
        #print(day, cost)
        if day != t:
            ans += min(C, t) * (day - t)
            t = day
        t += cost
    print(ans)

if __name__ == '__main__':
    main()