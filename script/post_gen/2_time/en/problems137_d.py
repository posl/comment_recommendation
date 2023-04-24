Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    B, A = zip(*sorted(zip(B, A), reverse=True))
    B = list(B)
    A = list(A)

    ans = 0
    for i in range(N):
        if A[i] <= M:
            ans += B[i]
            M -= A[i]
        else:
            break
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs = sorted(jobs, key=lambda x: x[0])
    ans = 0
    reward = 0
    for i in range(N):
        A, B = jobs[i]
        reward += B
        if A <= M:
            ans = max(ans, reward)
        else:
            break
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        if A <= M:
            jobs.append((A, B))
    jobs.sort()
    dp = [0] * (M + 1)
    for a, b in jobs:
        for i in range(M, a - 1, -1):
            dp[i] = max(dp[i], dp[i - a] + b)
    print(max(dp))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))

    jobs.sort(key=lambda x: x[0])

    ans = 0
    reward = 0
    for A, B in jobs:
        if A <= M:
            reward += B
            M -= A
            ans = max(ans, reward)

    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(key=lambda x: x[0])
    reward = 0
    jobs = []
    for i in range(N):
        if AB[i][0] <= M:
            reward += AB[i][1]
            jobs.append(AB[i][0])
            M -= 1
    jobs.sort()
    for i in range(len(jobs)):
        if jobs[i] <= M:
            reward -= 1
            M -= 1
    print(reward)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    jobs.sort(key=lambda x: x[0])
    dp = [0] * (M + 1)
    for i in range(N):
        a, b = jobs[i][0], jobs[i][1]
        for j in range(M, -1, -1):
            if j + a <= M:
                dp[j + a] = max(dp[j + a], dp[j] + b)
    print(max(dp))

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB = sorted(AB, key=lambda x: x[0])
    AB = sorted(AB, key=lambda x: x[1], reverse=True)
    dp = [0] * (M + 1)
    for a, b in AB:
        for i in range(M, -1, -1):
            if i + a <= M:
                dp[i + a] = max(dp[i + a], dp[i] + b)
    print(max(dp))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]

    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)

    days = 0
    reward = 0
    for job in jobs:
        if days + job[0] <= M:
            days += job[0]
            reward += job[1]

    print(reward)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        A, B = map(int, input().split())
        B.append((A, B))
    B.sort(key=lambda x: x[0])
    print(B)

=======
Suggestion 10

def solve(N, M, A, B):
    # Write your code here
    return 0
