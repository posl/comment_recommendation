Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    jobs.reverse()
    days = []
    for i in range(m):
        days.append(i + 1)
    days.reverse()
    total = 0
    for i in range(m):
        for j in range(n):
            if jobs[j][0] <= days[i]:
                total += jobs[j][1]
                jobs.pop(j)
                break
    print(total)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    ans = 0
    idx = 0
    for _ in range(M):
        while idx < N and jobs[idx][0] <= _ + 1:
            heapq.heappush(q, -jobs[idx][1])
            idx += 1
        if q:
            ans += -heapq.heappop(q)
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    jobs.reverse()
    days = []
    for i in range(M):
        days.append([])
    for i in range(N):
        A, B = jobs[i]
        if (M - A) >= 0:
            days[M - A].append(B)
    import heapq
    heap = []
    heapq.heapify(heap)
    ans = 0
    for i in range(M):
        for j in range(len(days[i])):
            heapq.heappush(heap, days[i][j])
        if len(heap) > 0:
            ans += heapq.heappop(heap)
    print(ans)

solve()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        a, b = map(int, input().split())
        jobs.append([a, b])
    jobs.sort()
    total = 0
    days = 0
    while days < M:
        max_reward = 0
        max_reward_index = 0
        for i in range(len(jobs)):
            if jobs[i][0] <= days:
                if jobs[i][1] > max_reward:
                    max_reward = jobs[i][1]
                    max_reward_index = i
            else:
                break
        if max_reward > 0:
            total += max_reward
            del jobs[max_reward_index]
        days += 1
    print(total)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    d = {}
    for j in range(1, m+1):
        while i < n and ab[i][0] <= j:
            if ab[i][1] in d:
                d[ab[i][1]] += 1
            else:
                d[ab[i][1]] = 1
            i += 1
        if d:
            k = max(d.keys())
            ans += k
            d[k] -= 1
            if d[k] == 0:
                del d[k]
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        if m >= a:
            ans += b
            m -= a
        else:
            ans += b * m
            break
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    from heapq import heappop, heappush
    h = []
    for i in range(1, M+1):
        while AB and AB[0][0] <= i:
            a, b = AB.pop(0)
            heappush(h, -b)
        if h:
            ans -= heappop(h)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: (x[1],x[0]))
    count = 0
    reward = 0
    for i in range(N):
        if count >= M:
            break
        if count + AB[i][0] <= M:
            count += AB[i][0]
            reward += AB[i][1]
        else:
            reward += AB[i][1]*(M-count)
            count = M
    print(reward)

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(tuple(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)
    #print(jobs)
    days = [0] * (M+1)
    ans = 0
    for i in range(N):
        for j in range(jobs[i][0], 0, -1):
            if days[j] == 0:
                days[j] = jobs[i][1]
                ans += jobs[i][1]
                break
    #print(days)
    print(ans)

=======
Suggestion 10

def solve():
    N,M = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[0])
    AB.append([M+1,0])

    import heapq
    hq = []
    heapq.heapify(hq)
    i = 0
    ans = 0
    for day in range(1,M+1):
        while AB[i][0] == day:
            heapq.heappush(hq, -AB[i][1])
            i += 1
        if len(hq) > 0:
            ans += -heapq.heappop(hq)
    print(ans)
