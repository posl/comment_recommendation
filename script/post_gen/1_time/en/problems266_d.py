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

    #dp[i][j] = i番目までのスヌークを見て、時間がjのときに取れる最大のスコア
    dp = [[0] * (T[N - 1] + 1) for i in range(N + 1)]
    for i in range(N):
        for j in range(T[i] + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + abs(X[i] - j) <= T[i]:
                dp[i + 1][X[i]] = max(dp[i + 1][X[i]], dp[i][j] + A[i])

    print(max(dp[N]))

=======
Suggestion 2

def main():
    N = int(input())
    X = [0]*N
    A = [0]*N
    T = [0]*N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0]*5 for _ in range(N+1)]
    for i in range(N):
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if T[i] >= abs(j-X[i]):
                dp[i+1][X[i]] = max(dp[i+1][X[i]], dp[i][j]+A[i])
    print(max(dp[N]))

=======
Suggestion 3

def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * 5 for _ in range(n + 1)]
    for i in range(n):
        for j in range(5):
            if j == s[i][1]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j] + s[i][2])
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - 1] + s[i][2])
    print(max(dp[-1]))

=======
Suggestion 4

def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if A[i][0] - A[i][1] == i:
                dp[i + 1][A[i][1]] = max(dp[i + 1][A[i][1]], dp[i][j] + A[i][2])
            if A[i][0] == i:
                dp[i + 1][A[i][1]] = max(dp[i + 1][A[i][1]], dp[i][j] + A[i][2], dp[i][j - 1] + A[i][2])
    print(max(dp[-1]))

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        A.append([T, X, A])
    A.sort()
    dp = [[0] * 5 for _ in range(N)]
    for i in range(N):
        for j in range(5):
            if A[i][1] == j:
                dp[i][j] = A[i][2]
    for i in range(1, N):
        for j in range(5):
            if A[i][0] == A[i - 1][0]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][A[i][1]] + A[i][2])
    print(max(dp[N - 1]))

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    S = sorted(S, key=lambda x: x[0])
    dp = [[0] * 5 for i in range(N)]
    for i in range(N):
        for j in range(5):
            if S[i][1] == j:
                dp[i][j] = S[i][2]
            else:
                dp[i][j] = 0
    for i in range(1, N):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + S[i][2])
        for j in range(5):
            if S[i][1] == j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + S[i][2])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
    print(max(dp[N - 1]))

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    S = sorted(S, key=lambda x: x[0])
    dp = [[0 for _ in range(5)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j == S[i-1][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + S[i-1][2])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][S[i-1][1]] + S[i-1][2])
    print(max(dp[N]))

=======
Suggestion 8

def solve():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort()

    dp = [[0] * 5 for _ in range(N+1)]
    for i in range(N):
        t, x, a = S[i]
        for j in range(5):
            if j == x:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + a if j > 0 else 0)
                dp[i+1][j] = max(dp[i+1][j], dp[i][j+1] + a if j < 4 else 0)
            else:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(max(dp[N]))

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    S = sorted(S, key=lambda x: x[0])
    dp = [0] * 5
    for i in range(N):
        t, x, a = S[i]
        dp[x] = max(dp[x], a)
        for j in range(5):
            if j != x:
                dp[j] = max(dp[j], dp[j] + a)
    print(max(dp))

=======
Suggestion 10

def main():
    N = int(input())
    #T,X,A = [list(map(int,input().split())) for _ in range(N)]
    T = [0]*(N+1)
    X = [0]*(N+1)
    A = [0]*(N+1)
    for i in range(N):
        T[i+1],X[i+1],A[i+1] = map(int,input().split())
    #print(N,T,X,A)
    #dp[i][j] = i番目までのスヌーケを捕まえたときの、最大のスコア
    dp = [[0]*5 for _ in range(N+1)]
    for i in range(N):
        for j in range(5):
            #i番目のスヌーケを捕まえない場合
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            #i番目のスヌーケを捕まえる場合
            if T[i+1] - T[i] >= abs(X[i+1] - j):
                dp[i+1][X[i+1]] = max(dp[i+1][X[i+1]],dp[i][j] + A[i+1])
    #print(dp)
    print(max(dp[N]))
