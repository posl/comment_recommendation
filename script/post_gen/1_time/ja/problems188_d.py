Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b+1, -c))
    AB.sort()
    ans = 0
    now = 0
    for i in range(len(AB)-1):
        now += AB[i][1]
        ans += min(now, C) * (AB[i+1][0] - AB[i][0])
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    service = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        service.append((a, c))
        service.append((b+1, -c))
    service.sort()
    ans = 0
    cost = 0
    prev = 0
    for i in range(2*N):
        ans += min(cost, C) * (service[i][0] - prev)
        cost += service[i][1]
        prev = service[i][0]
    print(ans)

main()

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += ABC[i][2]
        for j in range(i+1, N):
            if ABC[i][1] < ABC[j][0]:
                ans += C * (ABC[j][0] - ABC[i][1])
                break
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if i == 0:
            ans += AB[i][1] * C
        else:
            if AB[i][0] <= AB[i-1][1]:
                if AB[i][1] > AB[i-1][1]:
                    ans += (AB[i][1] - AB[i-1][1]) * C
            else:
                ans += (AB[i][1] - AB[i][0] + 1) * C
    print(ans)

main()

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][1] - AB[i][0] + 1
    ans *= C
    for i in range(N):
        if i == 0:
            ans -= C
            continue
        if AB[i][0] <= AB[i - 1][1]:
            ans -= C * (AB[i - 1][1] - AB[i][0] + 1)
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        ans += data[i][2] * (data[i][1] - data[i][0] + 1)
    for i in range(N):
        for j in range(i + 1, N):
            if data[i][1] < data[j][0]:
                break
            if data[i][1] <= data[j][1]:
                ans -= min(C, data[i][2]) * (data[i][1] - data[j][0] + 1)
            else:
                ans -= min(C, data[i][2]) * (data[j][1] - data[j][0] + 1)
    print(ans)

=======
Suggestion 7

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(N)]
    D.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if i == 0:
            ans += D[i][2] * (D[i][1] - D[i][0] + 1)
        else:
            ans += D[i][2] * (D[i][1] - D[i][0] + 1)
            for j in range(i):
                if D[j][1] >= D[i][0]:
                    ans -= min(D[j][2], D[i][2]) * (D[i][1] - max(D[j][1], D[i][0]) + 1)
    print(ans)

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)

    #各日にちにおける利用するサービスの個数
    use = [0]*(AB[-1][1]+1)
    for i in range(N):
        use[AB[i][0]] += 1
        use[AB[i][1]+1] -= 1
    #print(use)

    #各日にちにおける利用するサービスの個数の累積和
    for i in range(1, AB[-1][1]+1):
        use[i] += use[i-1]
    #print(use)

    #各日にちにおける利用するサービスの個数の累積和の最小値
    for i in range(1, AB[-1][1]+1):
        use[i] = min(use[i], use[i-1])
    #print(use)

    #各日にちにおけるサービスを利用するために支払う金額
    cost = [0]*(AB[-1][1]+1)
    for i in range(N):
        cost[AB[i][0]] += AB[i][2]
        cost[AB[i][1]+1] -= AB[i][2]
    #print(cost)

    #各日にちにおけるサービスを利用するために支払う金額の累積和
    for i in range(1, AB[-1][1]+1):
        cost[i] += cost[i-1]
    #print(cost)

    #各日にちにおけるサービスを利用するために支払う金額の累積和の最小値
    for i in range(1, AB[-1][1]+1):
        cost[i] = min(cost[i], cost[i-1])
    #print(cost)

    #各日にちにおけるサービスを利用

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]

    # すぬけプライムに加入する日、脱退する日を取得
    day = []
    for a, b, c in ABC:
        day.append((a, c))
        day.append((b + 1, -c))
    day.sort()

    # すぬけプライムに加入している日数を取得
    sum = 0
    cnt = 0
    for i in range(len(day) - 1):
        sum += day[i][1]
        cnt += min(C, sum) * (day[i + 1][0] - day[i][0])

    print(cnt)
