Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    jobs = sorted(zip(A, B))
    ans = 0
    i = 0
    while i < N:
        a, b = jobs[i]
        if a > M:
            break
        ans += b
        M -= a
        i += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    import heapq
    heap = []
    heapq.heapify(heap)
    score = 0
    idx = 0
    for d in range(M):
        while idx < N and jobs[idx][0] == d + 1:
            heapq.heappush(heap, -jobs[idx][1])
            idx += 1
        if len(heap) > 0:
            score += -heapq.heappop(heap)
    print(score)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs = sorted(jobs, key=lambda x: x[0])
    reward = 0
    days = 0
    while days < M:
        A, B = jobs.pop()
        if days + A > M:
            continue
        reward += B
        days += A
    print(reward)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append([A, B])
    jobs.sort()
    jobs.reverse()
    days = [0] * (M + 1)
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if days[j] != 0:
                if j + jobs[i][0] < M + 1:
                    if days[j + jobs[i][0]] == 0:
                        days[j + jobs[i][0]] = days[j] + jobs[i][1]
                    else:
                        days[j + jobs[i][0]] = max(days[j + jobs[i][0]], days[j] + jobs[i][1])
            elif j + jobs[i][0] < M + 1:
                days[j + jobs[i][0]] = jobs[i][1]
    print(max(days))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    for _ in range(M):
        while i < N and AB[i][0] <= _ + 1:
            AB[i][0] = 0
            i += 1
        if i == N:
            break
        ans += AB[i][1]
        AB[i][0] -= _ + 1
    print(ans)
main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    days = 0
    for job in jobs:
        if days + job[0] <= M:
            ans += job[1]
            days += job[0]
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))

    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)

    days = [0 for i in range(10**5+1)]
    for i in range(N):
        days[jobs[i][0]] += jobs[i][1]

    ans = 0
    for i in range(1, M+1):
        ans += days[i]
    print(ans)

=======
Suggestion 8

def solve(n, m, jobs):
    jobs.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m >= jobs[i][0]:
            ans += jobs[i][1]
            m -= 1
    return ans

n, m = map(int, input().split())
jobs = []
for i in range(n):
    a, b = map(int, input().split())
    jobs.append([a, b])
print(solve(n, m, jobs))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        jobs.append(tuple(map(int, input().split())))
    jobs.sort()
    jobs = jobs[::-1]
    day = m
    reward = 0
    while day > 0:
        max_reward = 0
        max_reward_index = -1
        for i in range(len(jobs)):
            if jobs[i][0] <= day:
                if jobs[i][1] > max_reward:
                    max_reward = jobs[i][1]
                    max_reward_index = i
        if max_reward_index > -1:
            reward += max_reward
            day -= 1
            jobs.pop(max_reward_index)
        else:
            break
    print(reward)

=======
Suggestion 10

def solve(n, m, ab):
    ab.sort()
    ab.reverse()
    ab = ab[:m]
    ab.sort(key=lambda x: x[1])
    ab.reverse()
    return sum(map(lambda x: x[1], ab))

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
print(solve(n, m, ab))
