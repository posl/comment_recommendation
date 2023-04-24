Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

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

=======
Suggestion 3

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

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    services = []
    for i in range(N):
        a, b, c = map(int, input().split())
        services.append((a, c))
        services.append((b + 1, -c))
    services.sort()
    ans = 0
    sum = 0
    last = 0
    for i in range(len(services)):
        if i == 0:
            last = services[i][0]
        if last != services[i][0]:
            ans += min(sum, C) * (services[i][0] - last)
            last = services[i][0]
        sum += services[i][1]
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        a = AB[i][0]
        b = AB[i][1]
        c = AB[i][2]
        ans += min(C, c) * (b - a + 1)
    print(ans)

=======
Suggestion 7

def main():
    N, C = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][2]
    ans *= C
    for i in range(N-1):
        for j in range(i+1, N):
            if AB[i][1] >= AB[j][0]:
                ans = min(ans, (AB[j][1]-AB[j][0]+1)*C*AB[j][2]+(AB[i][1]-AB[j][0]+1)*C*AB[i][2])
            else:
                ans = min(ans, (AB[j][1]-AB[j][0]+1)*C*AB[j][2]+(AB[i][1]-AB[i][0]+1)*C*AB[i][2])
    print(ans)

=======
Suggestion 8

def main():
    #input
    N, C = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(N)]
    ABC.sort(key=lambda x: x[0])

    #compute
    ans = 0
    for i in range(N):
        ans += ABC[i][2]
        ABC[i][1] += 1
    ABC.sort(key=lambda x: x[1])
    for i in range(N):
        ABC[i][0] += 1
    ABC.sort(key=lambda x: x[0])
    #print(ABC)

    for i in range(N):
        if i == 0:
            pass
        elif ABC[i][0] == ABC[i-1][0]:
            ABC[i][2] += ABC[i-1][2]
    #print(ABC)

    for i in range(N):
        if i == 0:
            pass
        elif ABC[i][1] == ABC[i-1][1]:
            ABC[i][2] -= ABC[i-1][2]
    #print(ABC)

    for i in range(N):
        if ABC[i][2] > C:
            ans += C*(ABC[i][1]-ABC[i][0])
        else:
            ans += ABC[i][2]*(ABC[i][1]-ABC[i][0])
    #print(ans)

    #output
    print(ans)

=======
Suggestion 9

def main():
    import sys
    from bisect import bisect_left
    from collections import defaultdict
    input = sys.stdin.readline
    N, C = map(int, input().split())
    service = [list(map(int, input().split())) for _ in range(N)]
    service.sort()
    #print(service)
    #print(N, C)
    #print(service)
    #print(service)
    s = defaultdict(int)
    for i in range(N):
        s[service[i][0]] += service[i][2]
        s[service[i][1] + 1] -= service[i][2]
    #print(s)
    d = [0]
    for i in range(1, 10 ** 9 + 1):
        d.append(d[-1] + s[i])
    #print(d)
    ans = 10 ** 20
    for i in range(1, 10 ** 9 + 1):
        ans = min(ans, d[bisect_left(d, C)])
    print(ans)

=======
Suggestion 10

def main():
    #入力
    N, C = map(int, input().split())
    ABC = [tuple(map(int, input().split())) for _ in range(N)]
    #初期化
    ABC.sort()
    #print(ABC)
    ans = 0
    for i in range(N):
        #print(i, ABC[i])
        ans += ABC[i][2]
        #print(ans)
        for j in range(i+1, N):
            #print(j, ABC[j])
            if ABC[i][1] >= ABC[j][0]:
                ans += min(ABC[j][2], C*(ABC[j][0]-ABC[i][1]))
            else:
                break
            #print(ans)
    print(ans)

main()
