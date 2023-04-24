Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = (v[0] + v[1]) / 2
    for i in range(2, N):
        ans = (v[i] + ans) / 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    V = sorted(list(map(int, input().split())))
    ans = (V[0] + V[1]) / 2
    for i in range(2, N):
        ans = (ans + V[i]) / 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N - 1):
        v[i + 1] = (v[i] + v[i + 1]) / 2
    print(v[N - 1])

=======
Suggestion 4

def main():
    N = int(input())
    V = list(map(int, input().split()))
    V.sort()
    while len(V) > 1:
        V.append((V.pop(0) + V.pop(0)) / 2)
    print(V[0])

=======
Suggestion 5

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v) > 1:
        v.append((v[0] + v[1]) / 2)
        del v[0]
        del v[0]
        v.sort()
    print(v[0])

=======
Suggestion 6

def main():
  N = int(input())
  v = list(map(int, input().split()))
  v.sort()

  for i in range(N-1):
    v[i+1] = (v[i] + v[i+1]) / 2

  print(v[-1])

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    max_v = v[-1]
    for i in range(n-1):
        max_v = (max_v + v[i]) / 2
    print(max_v)

=======
Suggestion 8

def max_value(N, v):
    v.sort()
    while len(v) > 1:
        v[0] = (v[0] + v[1]) / 2.0
        del v[1]
        v.sort()
    return v[0]

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))

    # dp[i][j] = i番目までの数字を使って、j個の数字を作ったときの最大値
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][1] = v[i]
    for i in range(2, n+1):
        for j in range(1, n+1):
            for k in range(j):
                dp[i][j] = max(dp[i][j], (dp[i-1][k] + dp[i-1][j-k]) / 2)
    print(dp[n][n])
