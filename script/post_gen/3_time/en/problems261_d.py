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

    # dp[i][j] = i番目までのコインを投げた時、連続でj回コインが表が出た時の最大値
    # dp[i][j] = max(dp[i-1][j], dp[i-C[j]][j-1] + X[i] + Y[j])
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - C[j - 1]][j - 1] + X[i - 1] + Y[j - 1])

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
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + X[i])
            for k in range(M):
                if j == C[k] - 1:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + Y[k])
    print(max(dp[N]))

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
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + Y[j])
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + X[i] + Y[j])
    print(dp[N])
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j < N:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
        for k in range(M):
            if j >= C[k]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - C[k]] + Y[k])
    print(max(dp[N]))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(M):
            dp[min(i+C[j], N)] = max(dp[min(i+C[j], N)], dp[i]+Y[j])
    print(dp[N])

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i],Y[i] = map(int,input().split())
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+X[i])
            if i+1>=C[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1-C[j]][j]+X[i]+Y[j])
    print(max(dp[N]))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * N
    Y = [0] * N
    for _ in range(M):
        c, y = map(int, input().split())
        C[c - 1] = c
        Y[c - 1] = y
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(i + 1, N):
            if C[j] == 0:
                break
            dp[j + 1] = max(dp[j + 1], dp[i] + X[i] * (j - i) + Y[j] * (j - i + 1))
    print(dp[N])

=======
Suggestion 10

def main():
    #input
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C_Y = [list(map(int, input().split())) for _ in range(M)]
    #compute
    C_Y.sort(key=lambda x: x[0], reverse=True)
    C, Y = zip(*C_Y)
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(M):
            if i-C[j]>=0:
                dp[i+1] = max(dp[i+1], dp[i-C[j]]+X[i]+Y[j])
    #output
    print(dp[N])
