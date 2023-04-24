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
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if X[i] == 1:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + Y[j])
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
    X.sort(reverse=True)
    Y.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += X[i]
        for j in range(M):
            if i + 1 >= C[j]:
                ans += Y[j] * ((i + 1) // C[j])
    print(ans)

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
            if i + C[j] <= N:
                dp[i + C[j]] = max(dp[i + C[j]], dp[i] + Y[j])

    print(max(dp))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
        for j in range(M):
            if C[j] <= i:
                dp[i] = max(dp[i], dp[i - C[j]] + Y[j])
    print(dp[N])

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
        dp[i + 1] = dp[i] + X[i]
        for j in range(M):
            if i + 1 >= C[j]:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - C[j]] + Y[j])

    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i], dp[i] + X[i])
        for j in range(M):
            if i + 1 >= C[j]:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - C[j]] + Y[j])
    print(dp[N])

=======
Suggestion 7

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
            if i + C[j] > N:
                continue
            dp[i + C[j]] = max(dp[i + C[j]], dp[i] + Y[j])
    print(dp[N])

=======
Suggestion 8

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
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i] + X[i])
        for j in range(M):
            if i - C[j] >= 0:
                dp[i+1] = max(dp[i+1], dp[i-C[j]] + Y[j])

    print(dp[-1])

=======
Suggestion 9

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
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(M):
            if i+1 >= C[j]:
                dp[i+1] = max(dp[i+1], dp[i+1-C[j]]+Y[j])
    print(dp[N])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonus = []
    for _ in range(M):
        C, Y = map(int, input().split())
        bonus.append((C, Y))
    bonus.sort(reverse=True)
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for C, Y in bonus:
            if i + 1 >= C:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - C] + Y)
    print(dp[N])
