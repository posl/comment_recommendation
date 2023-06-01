Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort()
    #print(ab)
    ans = 0
    i = 0
    while m > 0:
        if i >= n:
            break
        a, b = ab[i]
        if m >= a:
            ans += b
            m -= a
        else:
            break
        i += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    # print(n, m)
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    # print(ab)
    ab.sort(key=lambda x: x[0])
    # print(ab)
    ans = 0
    for i in range(n):
        if ab[i][0] <= m:
            ans += ab[i][1]
            m -= ab[i][0]
        else:
            ans += m * ab[i][1]
            break
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    import heapq
    h = []
    i = 0
    res = 0
    for d in range(1, M+1):
        while i < N and jobs[i][0] <= d:
            heapq.heappush(h, -jobs[i][1])
            i += 1
        if h:
            res -= heapq.heappop(h)
    print(res)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))

    jobs.sort(key=lambda x: x[0])
    # print(jobs)
    # print(m)

    if m == 0:
        print(0)
        return

    ans = 0
    for a, b in jobs:
        if m >= a:
            ans += b
            m -= a
        else:
            ans += m
            break
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    # print(AB)
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    ab.sort(key=lambda x: x[0])
    # print(ab)
    import heapq
    hq = []
    heapq.heapify(hq)
    ans = 0
    i = 0
    for d in range(1, m+1):
        while i < n and ab[i][0] <= d:
            heapq.heappush(hq, -ab[i][1])
            i += 1
        if hq:
            ans -= heapq.heappop(hq)
    print(ans)

=======
Suggestion 7

def max_reward(n, m, jobs):
    jobs.sort(key=lambda x:x[1])
    ans = 0
    for i in range(m):
        if len(jobs) == 0:
            break
        ans += jobs.pop()[1]
    return ans

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    job = []
    for _ in range(n):
        job.append(list(map(int, input().split())))
    job.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if job[i][0] <= m:
            ans += job[i][1]
            m -= job[i][0]
        else:
            ans += job[i][1] * m
            break
    print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    # 按照结束时间从小到大排序
    ab.sort(key=lambda x: x[0])

    # 从今天开始，一共可以工作的天数
    t = m + 1

    # dp[i][j]表示从第i个工作开始，一共工作了j天所能获得的最大奖励
    dp = [[0] * t for _ in range(n + 1)]

    # 从最后一个工作开始
    for i in range(n - 1, -1, -1):
        # 从第i个工作开始，最多可以工作的天数
        for j in range(t):
            # 从第i个工作开始，工作j天所能获得的最大奖励
            # 1.如果第i个工作的结束时间超过了总天数，那么第i个工作不能接受，所以从第i+1个工作开始工作j天所能获得的最大奖励就是从第i+1个工作开始工作j天所能获得的最大奖励
            # 2.如果第i个工作的结束时间没有超过总天数，那么第i个工作可以接受，所以从第i个工作开始工作j天所能获得的最大奖励就是从第i+1个工作开始工作j+1天所能获得的最大奖励加上第i个工作的奖励
            if ab[i][0] + j > m:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1] + ab[i][1])

    print(dp[0][0])

=======
Suggestion 10

def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    res = 0
    for i in range(n):
        if m >= ab[i][0]:
            res += ab[i][1]
            m -= 1
    print(res)
