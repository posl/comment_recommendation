Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x:x[0])
    result = 0
    i = 0
    while m > 0:
        if i == n:
            break
        if m >= jobs[i][0]:
            result += jobs[i][1]
            m -= jobs[i][0]
        else:
            break
        i += 1
    print(result)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])
    day = 0
    reward = 0
    while day < M:
        max_reward = 0
        max_reward_index = -1
        for i, (a, b) in enumerate(jobs):
            if a <= day:
                continue
            if b > max_reward:
                max_reward = b
                max_reward_index = i
        if max_reward_index == -1:
            break
        reward += max_reward
        day += 1
        del jobs[max_reward_index]
    print(reward)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    #print(jobs)
    i = 0
    reward = 0
    days = 0
    while days < M:
        if i >= N:
            break
        if days + jobs[i][0] <= M:
            reward += jobs[i][1]
            days += jobs[i][0]
        else:
            break
        i += 1
    print(reward)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: (x[0], x[1]))
    print(AB)
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))

    jobs.sort(key=lambda x:x[0])
    #print(jobs)
    total = 0
    for i in range(N):
        if jobs[i][0] <= M:
            total += jobs[i][1]
            M -= 1
        else:
            break
    print(total)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(N)])
    ans = 0
    i = 0
    import heapq
    h = []
    for day in range(1, M+1):
        while i < N and AB[i][0] <= day:
            heapq.heappush(h, -AB[i][1])
            i += 1
        if h:
            ans -= heapq.heappop(h)
    return ans

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    jobs = [tuple(map(int, input().split())) for _ in range(n)]
    jobs.sort(key=lambda x: x[0])
    # print(jobs)

    ans = 0
    for i in range(m):
        if len(jobs) == 0:
            break
        max_reward = 0
        max_reward_index = -1
        for j in range(len(jobs)):
            if jobs[j][0] <= i + 1 and max_reward < jobs[j][1]:
                max_reward = jobs[j][1]
                max_reward_index = j
            else:
                break
        if max_reward_index != -1:
            ans += max_reward
            jobs.pop(max_reward_index)
    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    jobs = []
    for i in range(N):
        A,B = map(int,input().split())
        jobs.append((A,B))
    jobs.sort()
    jobs.reverse()
    reward = 0
    for i in range(1,M+1):
        while jobs and jobs[-1][0] <= i:
            reward += jobs[-1][1]
            jobs.pop()
    print(reward)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    jobs = [tuple(map(int, input().split())) for i in range(n)]
    jobs.sort(key=lambda x: x[0])
    import heapq
    heap = []
    ans = 0
    for d in range(1, m+1):
        while jobs and jobs[0][0] == d:
            heapq.heappush(heap, -jobs[0][1])
            jobs.pop(0)
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)

solve()

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    AB = [AB[i] for i in range(N) if AB[i][0] <= M]
    N = len(AB)
    dp = [0] * (N+1)
    for i in range(N):
        dp[i+1] = max(dp[i], dp[i] + AB[i][1])
    print(dp[N])
