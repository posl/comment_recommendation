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
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N + 1):
            if dp[i][j] > dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j]
            if j > 0 and dp[i][j - 1] + X[i] > dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j - 1] + X[i]
            for k in range(M):
                if j >= C[k] and dp[i][j - C[k]] + X[i] + Y[k] > dp[i + 1][j]:
                    dp[i + 1][j] = dp[i][j - C[k]] + X[i] + Y[k]
    print(dp[N][N])

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
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + X[i] + Y[j])
    print(max(dp))

=======
Suggestion 3

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
            dp[min(N, i + C[j])] = max(dp[min(N, i + C[j])], dp[i] + X[i] + Y[j])
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for _ in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i])
        for j in range(M):
            if i+C[j] <= N:
                dp[i+C[j]] = max(dp[i+C[j]], dp[i]+X[i]+Y[j])
    print(dp[-1])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    #print(N, M)
    #print(X)
    #print(C)
    #print(Y)
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(M):
            if i+C[j] > N:
                continue
            dp[i+C[j]] = max(dp[i+C[j]], dp[i]+Y[j])
    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0]*(N+1)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = dp[i] + X[i]
        for j in range(M):
            if i+1 >= C[j]:
                dp[i+1] = max(dp[i+1], dp[i+1-C[j]] + Y[j] + X[i])
    print(dp[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonus = [[0, 0] for _ in range(M)]
    for i in range(M):
        bonus[i] = list(map(int, input().split()))
    bonus.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + bonus[j][0] > N:
                break
            dp[i + bonus[j][0]] = max(dp[i + bonus[j][0]], dp[i] + bonus[j][1])
    print(dp[N])

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = [0]*n
    y = [0]*n
    for i in range(m):
        c[i],y[i] = map(int,input().split())
    dp = [0]*(n+1)
    dp[0] = 0
    for i in range(n):
        dp[i+1] = dp[i]+x[i]
        for j in range(m):
            if i+1-c[j]>=0:
                dp[i+1] = max(dp[i+1],dp[i+1-c[j]]+y[j])
    print(dp[n])

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = defaultdict(int)
    for _ in range(M):
        c, y = map(int, input().split())
        C[c] = y
    dp = [0 for _ in range(N+1)]
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(i+1, N):
            if C[j-i] > 0:
                dp[j+1] = max(dp[j+1], dp[i]+X[i]+C[j-i]*(j-i))
    print(dp[N])

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
