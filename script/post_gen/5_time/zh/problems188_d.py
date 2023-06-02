Synthesizing 10/10 solutions

=======
Suggestion 1

def read_int_list():
    return list(map(int, input().split()))

N, C = read_int_list()
services = []
for _ in range(N):
    services.append(read_int_list())

=======
Suggestion 2

def solve(n,c,events):
    events.sort()
    dp = [0]
    for day in range(1,events[-1][1]+1):
        dp.append(dp[-1]+c)
        for a,b,p in events:
            if b < day:
                continue
            if day < a:
                dp[-1] += p
            else:
                dp[-1] += min(p,(day-a+1)*c)
    return min(dp)

n,c = map(int,input().split())
events = []
for _ in range(n):
    a,b,p = map(int,input().split())
    events.append((a,b,p))
print(solve(n,c,events))

=======
Suggestion 3

def solve():
    N,C = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)

    #print(A)
    #print(B)
    #print(C)

=======
Suggestion 4

def solve():
    n,c = map(int, input().split())
    d = {}
    for _ in range(n):
        a,b,c = map(int, input().split())
        d[a] = d.get(a,0) + c
        d[b+1] = d.get(b+1,0) - c
    d = sorted(d.items())
    ans = 0
    s = 0
    t = 0
    for i in range(len(d)-1):
        s += d[i][1]
        t += d[i+1][0] - d[i][0]
        if s > c:
            ans += c * t
        else:
            ans += s * t
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    service = []
    for i in range(N):
        service.append(list(map(int, input().split())))
    service.sort()
    #print(service)

    #计算每天的费用
    daily_cost = [0] * (service[-1][1] + 1)
    for i in range(N):
        daily_cost[service[i][0] - 1] += service[i][2]
        daily_cost[service[i][1]] -= service[i][2]
    #print(daily_cost)

    #计算每天的费用累计和
    daily_cost_sum = [0] * (service[-1][1] + 1)
    daily_cost_sum[0] = daily_cost[0]
    for i in range(1, service[-1][1] + 1):
        daily_cost_sum[i] = daily_cost_sum[i - 1] + daily_cost[i]
    #print(daily_cost_sum)

    #计算每天的费用累计和的最小值
    daily_cost_sum_min = [0] * (service[-1][1] + 1)
    daily_cost_sum_min[0] = daily_cost_sum[0]
    for i in range(1, service[-1][1] + 1):
        daily_cost_sum_min[i] = min(daily_cost_sum_min[i - 1], daily_cost_sum[i])
    #print(daily_cost_sum_min)

    #计算最小总金额
    total_cost = 0
    for i in range(service[-1][1] + 1):
        if daily_cost_sum_min[i] * C < daily_cost_sum[i]:
            total_cost += daily_cost_sum_min[i] * C
        else:
            total_cost += daily_cost_sum[i]
    print(total_cost)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    A, B, C = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)

    # 1. 按照开始时间排序
    # 2. 合并时间段
    # 3. 遍历时间段，计算总费用
    # 4. 比较总费用和C，取最小值
    # 5. 如果最小值小于C，输出最小值；否则输出C
    # 6. 如果没有合并时间段，输出总费用

    # 1. 按照开始时间排序
    AB = sorted(zip(A, B, C), key=lambda x: x[0])
    # 2. 合并时间段
    AB = merge(AB)
    # 3. 遍历时间段，计算总费用
    cost = 0
    for a, b, c in AB:
        cost += c * (b - a + 1)
    # 4. 比较总费用和C，取最小值
    cost = min(cost, C)
    # 5. 如果最小值小于C，输出最小值；否则输出C
    print(cost)

=======
Suggestion 7

def solve():
    N, C = map(int, input().split())
    events = []
    for i in range(N):
        a, b, c = map(int, input().split())
        events.append((a, c))
        events.append((b+1, -c))
    events.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in events:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)

solve()

=======
Suggestion 8

def main():
    n, c = map(int, input().split())
    a = [0] * n
    b = [0] * n
    cost = [0] * n
    for i in range(n):
        a[i], b[i], cost[i] = map(int, input().split())
    max_day = max(b)
    dp = [0] * (max_day + 1)
    for i in range(n):
        dp[a[i] - 1] += cost[i]
        dp[b[i]] -= cost[i]
    for i in range(1, max_day + 1):
        dp[i] += dp[i - 1]
    print(min(c, min(dp)))

=======
Suggestion 9

def main():
    N,C = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    print(N,C,A,B,C)

=======
Suggestion 10

def solve():
    N, C = map(int, input().split())
    service = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        service.append((a, c))
        service.append((b + 1, -c))
    service.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in service:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)
