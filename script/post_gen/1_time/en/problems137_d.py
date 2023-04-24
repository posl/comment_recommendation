Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A, B = zip(*sorted(zip(A, B), reverse=True))

    dp = [0] * (M + 1)
    for i in range(N):
        for j in range(M, 0, -1):
            if j - A[i] >= 0:
                dp[j] = max(dp[j], dp[j - A[i]] + B[i])
    print(dp[M])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    reward = 0
    day = 1
    for A, B in jobs:
        if A <= day:
            continue
        if A - day > M:
            break
        M -= A - day
        day = A
        reward += B
    print(reward)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        jobs.append(tuple(map(int, input().split())))
    jobs.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    i = 0
    while i < N and jobs[i][1] > 0:
        if M - jobs[i][0] >= 0:
            M -= jobs[i][0]
            ans += jobs[i][1]
        else:
            break
        i += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    dp = [0] * (M+1)
    for i in range(N):
        for j in range(M, 0, -1):
            if j >= jobs[i][0]:
                dp[j] = max(dp[j], dp[j-jobs[i][0]] + jobs[i][1])
    print(max(dp))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    reward = 0
    for i in range(N):
        if jobs[i][0] <= M:
            reward += jobs[i][1]
            M -= jobs[i][0]
        else:
            break
    print(reward)

=======
Suggestion 6

def main():
    N, M = [int(x) for x in input().split()]
    AB = [[int(x) for x in input().split()] for _ in range(N)]
    AB.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * (M + 1)
    for i in range(N):
        a, b = AB[i]
        for j in range(M - a, -1, -1):
            dp[j + a] = max(dp[j + a], dp[j] + b)
    print(max(dp))

=======
Suggestion 7

def main():
    # Input
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])

    # Solve
    AB.sort()
    ans = 0
    day = 0
    for i in range(N):
        if day + AB[i][0] <= M:
            day += AB[i][0]
            ans += AB[i][1]
        else:
            break

    # Output
    print(ans)

main()

=======
Suggestion 8

def solve(n, m, a, b):
    a = [0] + a
    b = [0] + b
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j - a[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - a[i]] + b[i])
    return dp[n][m]

=======
Suggestion 9

def main():
    N, M = map(int,input().split())
    job = []
    for i in range(N):
        a, b = map(int,input().split())
        job.append((a,b))
    job.sort()
    dp = [0]*(M+1)
    for i in range(N):
        a, b = job[i]
        for j in reversed(range(M+1)):
            if j+a <= M:
                dp[j+a] = max(dp[j+a], dp[j]+b)
    print(max(dp))

=======
Suggestion 10

def main():
    from bisect import bisect_left
    import heapq

    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A, B = zip(*sorted(zip(A, B), key=lambda x: x[0]))
    B = list(B)
    A = list(A)

    # print(A)
    # print(B)

    ans = 0
    heap = []
    for i in range(M):
        # print(i, ans, heap)
        idx = bisect_left(A, i+1)
        for j in range(idx):
            heapq.heappush(heap, -B[j])
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)
