Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            if j == 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            else:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + X[i])
                if j >= C[i]:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j-C[i]] + Y[i])
    print(max(dp[N]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = dp[i] + X[i]
        for j in range(M):
            if i + 1 - C[j] >= 0:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - C[j]] + X[i] + Y[j])
    print(dp[N])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        dp = [0] * (N + 1)
        for j in range(i + 1):
            dp[j + 1] = max(dp[j + 1], dp[j] + X[j])
            for k in range(M):
                if j + C[k] <= N:
                    dp[j + C[k]] = max(dp[j + C[k]], dp[j] + Y[k])
        ans = max(ans, dp[N])
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    ans = 0
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + Y[j])
    print(max(dp))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + Y[j])
    print(dp[N])

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())

    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i] + x[i])
        for j in range(m):
            if i + c[j] <= n:
                dp[i + c[j]] = max(dp[i + c[j]], dp[i] + y[j])

    print(dp[n])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * (N + 1)
    Y = [0] * (N + 1)
    for _ in range(M):
        c, y = map(int, input().split())
        C[c] = c
        Y[c] = y

    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
        if C[i] > 0:
            dp[i] = max(dp[i], dp[i - C[i]] + X[i - 1] + Y[C[i]])

    print(max(dp))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c1, y1 = map(int, input().split())
        c.append(c1)
        y.append(y1)

    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(n + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            if j in c:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + y[c.index(j)])
    print(max(dp[n]))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = [0 for i in range(n)]
    y = [0 for i in range(n)]
    for i in range(m):
        c[i],y[i] = map(int,input().split())
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    for i in range(n):
        dp[i+1] = max(dp[i+1],dp[i]+x[i])
        for j in range(m):
            if i+1-c[j]>=0:
                dp[i+1] = max(dp[i+1],dp[i+1-c[j]]+y[j])
    print(dp[n])

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c0,y0 = map(int,input().split())
        c.append(c0)
        y.append(y0)
    dp = [0]*(n+1)
    dp[0] = x[0]
    for i in range(1,n):
        dp[i] = dp[i-1]+x[i]
        for j in range(m):
            if i+1>=c[j]:
                dp[i] = max(dp[i],dp[i-c[j]]+x[i]+y[j]*(c[j]-1))
    print(max(dp))
    return
