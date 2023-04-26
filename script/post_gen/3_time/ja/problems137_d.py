Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    ans = 0
    que = []
    for i in range(M):
        while AB and AB[0][0] == i + 1:
            a, b = AB.pop(0)
            heapq.heappush(que, -b)

        if que:
            ans -= heapq.heappop(que)

    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    job = []
    for i in range(N):
        A, B = map(int, input().split())
        job.append([A, B])
    job.sort(key=lambda x: x[0])
    #print(job)
    ans = 0
    import heapq
    hq = []
    for i in range(M):
        for j in range(N):
            if job[j][0] == i+1:
                heapq.heappush(hq, -job[j][1])
        if hq:
            ans += -heapq.heappop(hq)
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
    ans = 0
    i = 0
    import heapq
    q = []
    for j in range(1, M+1):
        while i < N and jobs[i][0] <= j:
            heapq.heappush(q, -jobs[i][1])
            i += 1
        if len(q) > 0:
            ans -= heapq.heappop(q)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    i = 0
    ans = 0
    for day in range(1, M+1):
        while i < N and AB[i][0] == day:
            heapq.heappush(P, -AB[i][1])
            i += 1
        if P:
            ans -= heapq.heappop(P)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([M+1, 0])
    ans = 0
    q = []
    for i in range(N+1):
        while q and q[0][0] < AB[i][0]:
            ans += heapq.heappop(q)[1]
        heapq.heappush(q, [-AB[i][1], AB[i][1]])
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    que = []
    for i in range(1, M + 1):
        for a, b in AB:
            if a == i:
                que.append(b)
            else:
                break
        if que:
            ans += que.pop()
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    import heapq
    heap = []
    for i in range(1, M+1):
        for a, b in AB:
            if a == i:
                heapq.heappush(heap, -b)
            else:
                break
        if heap:
            ans -= heapq.heappop(heap)
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    q = []
    for i in range(1, m + 1):
        while ab and ab[0][0] <= i:
            _, b = ab.pop(0)
            heapq.heappush(q, -b)
        if q:
            ans += -heapq.heappop(q)
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort()
    jobs.append([M+1, 0])
    ans = 0
    dp = [0] * (M+1)
    for i in range(M):
        dp[i+1] = max(dp[i], dp[i+1])
        if jobs[0][0] == i+1:
            dp[i+1] = max(dp[i+1], jobs[0][1])
            jobs.pop(0)
        dp[i+jobs[0][0]] = max(dp[i+jobs[0][0]], dp[i] + jobs[0][1])
    print(dp[M])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])

    B = [0]
    for i in range(N):
        B.append(AB[i][1])
    B.sort(reverse=True)

    ans = 0
    for i in range(N):
        if AB[i][0] <= M:
            ans += B[AB[i][0]]
            M -= 1
    print(ans)
