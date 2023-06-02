Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, raw_input().split())
    AB = []
    for i in range(N):
        AB.append(map(int, raw_input().split()))
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
    print ans

=======
Suggestion 2

def solve(n, m, a, b):
    # 从第i项工作开始，可以获得的最大总奖励
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        # 从第i项工作开始，可以获得的最大总奖励
        dp[i] = max(dp[i + 1], dp[i + a[i]] + b[i])
    return dp[0]

=======
Suggestion 3

def max_reward(n, m, work):
    work.sort(key=lambda x: x[0])
    reward = 0
    for i in range(n):
        if work[i][0] <= m:
            m += work[i][1]
            reward += work[i][1]
        else:
            break
    return reward

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append([a, b])
    ab.sort(key=lambda x: x[0])
    import heapq
    import bisect
    ans = 0
    heap = []
    for i in range(1, m+1):
        while ab and ab[0][0] <= i:
            a, b = ab.pop(0)
            heapq.heappush(heap, -b)
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    from collections import deque
    q = deque()
    ans = 0
    i = 0
    for day in range(1, m + 1):
        while i < n and ab[i][0] == day:
            q.append(ab[i][1])
            i += 1
        if q:
            ans += max(q)
            q.remove(max(q))
    print(ans)
solve()

=======
Suggestion 7

def main():
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    i = 0
    ans = 0
    for _ in range(m):
        while i < n and ab[i][0] <= _ + 1:
            ans = max(ans, ab[i][1])
            i += 1
        print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    #print(jobs)
    reward = 0
    while M > 0:
        max_reward = 0
        max_reward_idx = -1
        for i in range(len(jobs)):
            if jobs[i][0] <= M and jobs[i][1] > max_reward:
                max_reward = jobs[i][1]
                max_reward_idx = i
        if max_reward_idx >= 0:
            reward += max_reward
            M -= jobs[max_reward_idx][0]
            del jobs[max_reward_idx]
        else:
            break
    print(reward)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    jobs = []
    for i in range(n):
        a,b = map(int,input().split())
        jobs.append((a,b))
    jobs.sort(key=lambda x:x[0])
    #print(jobs)
    #dp[i][j]表示前i个工作中，完成j个工作的最大奖励
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+jobs[i-1][1]) if j>=jobs[i-1][0] else dp[i-1][j]
    print(dp[n][m])

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    works = []
    for _ in range(n):
        a, b = map(int, input().split())
        works.append((a, b))
    works.sort(key=lambda x: x[0])
    ans = 0
    for a, b in works:
        if m >= a:
            m -= a
            ans += b
    print(ans)
