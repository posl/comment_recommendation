Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0] * 5 for i in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if T[i] - j >= 0:
                dp[i + 1][X[i]] = max(dp[i + 1][X[i]], dp[i][j] + A[i])
    ans = 0
    for i in range(5):
        ans = max(ans, dp[N][i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0] * 5 for i in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if T[i] >= abs(X[i] - j):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][X[i]] + A[i])
    print(max(dp[N]))

main()

=======
Suggestion 3

def main():
    N = int(input())
    T, X, A = [], [], []
    for _ in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)

    # dp[i][j] = i番目までのスヌークを捕まえたときの、座標jでの最大のスヌークの総和
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + A[i] (j == X[i])
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) (j != X[i])
    dp = [[0] * 5 for _ in range(N)]
    dp[0][X[0]] = A[0]
    for i in range(1, N):
        for j in range(5):
            if j == X[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + A[i]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])

    print(max(dp[N-1]))

=======
Suggestion 4

def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[[0] * 5 for _ in range(5)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            for k in range(5):
                if j != k:
                    dp[i + 1][k][X[i]] = max(dp[i + 1][k][X[i]], dp[i][j][k] + A[i])
                if T[i] >= abs(j - k):
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
    print(max([dp[N][j][k] for j in range(5) for k in range(5)]))

=======
Suggestion 5

def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0] * 5 for _ in range(N)]
    for i in range(N):
        for j in range(5):
            if j == X[i]:
                dp[i][j] = dp[i-1][j] + A[i]
            else:
                dp[i][j] = dp[i-1][j]
        for j in range(5):
            if T[i] - 1 == T[i-1] and j == X[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][X[i]] + A[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
    print(max(dp[N-1]))

=======
Suggestion 6

def main():
    N = int(input())
    Snuke = []
    for i in range(N):
        T, X, A = map(int, input().split())
        Snuke.append([T, X, A])
    Snuke = sorted(Snuke, key=lambda x: x[0])
    #print(Snuke)

    dp = [[0] * 5 for i in range(N+1)]
    for i in range(N):
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if Snuke[i][1] == j:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + Snuke[i][2])
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1])
            if j < 4:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j+1])
    #print(dp)
    print(max(dp[-1]))

=======
Suggestion 7

def main():
    N = int(input())
    Snuke = []
    for i in range(N):
        T, X, A = map(int, input().split())
        Snuke.append((T, X, A))
    Snuke.sort()

    dp = [[0 for j in range(5)] for i in range(N)]
    for i in range(N):
        for j in range(5):
            if i == 0:
                if Snuke[i][1] == j:
                    dp[i][j] = Snuke[i][2]
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j]

                if Snuke[i][1] == j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + Snuke[i][2])
                if Snuke[i][1] == j - 1 and Snuke[i][0] - Snuke[i - 1][0] >= abs(j - (j - 1)):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + Snuke[i][2])
                if Snuke[i][1] == j + 1 and Snuke[i][0] - Snuke[i - 1][0] >= abs(j - (j + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + Snuke[i][2])

    print(max(dp[N - 1]))

=======
Suggestion 8

def main():
    N = int(input())
    snukes = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        snukes.append((T, X, A))
    snukes.sort()
    dp = [[0 for _ in range(5)] for _ in range(N+1)]
    for i in range(N):
        T, X, A = snukes[i]
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j == X:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + A)
            if j < X:
                dp[i+1][X] = max(dp[i+1][X], dp[i][j] + A)
            if j > X:
                dp[i+1][X] = max(dp[i+1][X], dp[i][j] + A)
    print(max(dp[-1]))

=======
Suggestion 9

def main():
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]
    dp = [[0] * 5 for i in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = dp[i][j]
        dp[i + 1][S[i][1]] = max(dp[i + 1][S[i][1]], dp[i][S[i][1]])
        for j in range(5):
            if j == S[i][1]:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + S[i][2] * (S[i][0] - i))
    print(max(dp[N]))

=======
Suggestion 10

def main():
    N = int(input())
    #dp[t][i] = t秒目に座標iにいる時の最大スコア
    dp = [[0]*5 for _ in range(10**5+1)]
    for _ in range(N):
        T, X, A = map(int, input().split())
        for i in range(5):
            if i == X:
                dp[T][i] = max(dp[T-1][i] + A, dp[T][i])
            else:
                dp[T][i] = max(dp[T-1][i], dp[T][i])
        for i in range(5):
            dp[T+1][i] = max(dp[T][i], dp[T+1][i])
    print(max(dp[-1]))
