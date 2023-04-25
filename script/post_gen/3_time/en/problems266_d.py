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

    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if T[i] - abs(j - X[i]) >= 0:
                dp[i + 1][X[i]] = max(dp[i + 1][X[i]], dp[T[i] - abs(j - X[i])][j] + A[i])
    print(max(dp[N]))

=======
Suggestion 2

def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #dp[t][x] := t時点でxにいる時の最大の取得可能なスヌーケの合計サイズ
    dp = [[0] * 5 for _ in range(10 ** 5 + 1)]
    for i in range(N):
        for j in range(5):
            dp[T[i]][j] = max(dp[T[i]][j], dp[T[i] - 1][j])
        dp[T[i]][X[i]] = max(dp[T[i]][X[i]], dp[T[i] - 1][X[i]] + A[i])
    print(max(dp[T[-1]]))

=======
Suggestion 3

def main():
    N = int(input())
    X = []
    T = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        X.append(x)
        T.append(t)
        A.append(a)
    dp = [[0 for j in range(5)] for i in range(N)]
    for i in range(N):
        for j in range(5):
            if i == 0:
                if X[i] == j:
                    dp[i][j] = A[i]
            else:
                dp[i][j] = dp[i-1][j]
                if X[i] == j:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + A[i])
                if j < 4:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1] + A[i])
    print(max(dp[N-1]))

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())

    #初期化
    dp = [[0] * 5 for _ in range(N + 1)]

    #dp[i][j] = i番目のスヌークまで見て、座標jにいるときの最大値
    for i in range(N):
        for j in range(5):
            if T[i] - j < 0:
                continue
            if T[i] - j > i:
                continue
            if X[i] == j:
                dp[i + 1][j] = max(dp[i][j] + A[i], dp[i][j - 1], dp[i][j + 1])
            else:
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j + 1])

    #出力
    print(dp[N][0])

=======
Suggestion 5

def main():
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 5 for _ in range(N+1)]
    for i in range(N):
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if S[i][0] == i+1:
            dp[i+1][S[i][1]] = max(dp[i+1][S[i][1]], dp[i][S[i][1]] + S[i][2])
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + S[i][2])
    print(max(dp[-1]))

=======
Suggestion 6

def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    txa = [[0, 0, 0]] + txa + [[10**5 + 1, 0, 0]]
    ans = 0
    for i in range(n + 1):
        dt = txa[i + 1][0] - txa[i][0]
        dx = abs(txa[i + 1][1] - txa[i][1])
        if dt < dx:
            print(0)
            return
        elif (dt - dx) % 2 == 0:
            ans += txa[i][2]
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = []
    for i in range(n):
        t, x, a = map(int, input().split())
        a.append((t, x, a))
    a.sort()
    dp = [[0] * 5 for i in range(n + 1)]
    for i in range(n):
        t, x, a = a[i]
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j == x:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a)
            if abs(j - x) <= t - i:
                dp[i + 1][x] = max(dp[i + 1][x], dp[i][j] + a)
    print(max(dp[n]))

=======
Suggestion 8

def main():
    N = int(input())
    Snuke = [[int(i) for i in input().split()] for _ in range(N)]
    Snuke.sort()
    dp = [[0 for _ in range(5)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(5):
            dp[i][j] = max(dp[i-1][j], dp[i][j])
            if Snuke[i-1][0] >= abs(j-Snuke[i-1][1]):
                dp[i][j] = max(dp[i][j], dp[i-1][Snuke[i-1][1]] + Snuke[i-1][2])
    print(max(dp[N]))

=======
Suggestion 9

def main():
    #input
    N = int(input())
    XTs = [[*map(int, input().split())] for _ in range(N)]
    XTs.sort(key=lambda x: x[0])
    XTs = [[0,0,0]] + XTs

    #solve
    dp = [[[0]*5 for _ in range(5)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(5):
            for k in range(5):
                t, x, a = XTs[i]
                if j == k:
                    if t == XTs[i-1][0] + abs(j-x):
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][k-1] + a)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
                else:
                    if t == XTs[i-1][0] + abs(j-x):
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][k] + a)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

    #output
    print(max(dp[N][0][0], dp[N][0][1], dp[N][0][2], dp[N][0][3], dp[N][0][4]))

=======
Suggestion 10

def main():
    N = int(input())
    info = []
    for i in range(N):
        info.append(list(map(int, input().split())))
    info.sort()
    dp = [[0] * 5 for _ in range(100005)]
    for i in range(N):
        t, x, a = info[i]
        for j in range(5):
            dp[t][j] = max(dp[t][j], dp[t - 1][j])
        dp[t][x] = max(dp[t][x], dp[t - 1][x] + a)
    print(max(dp[-1]))
