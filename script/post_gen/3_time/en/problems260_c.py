Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    N, X, Y = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][1] = 1
    for i in range(N):
        for j in range(N - i + 1):
            dp[i + j][j] += dp[i][j] * (i + j)
            dp[i + j - 1][j + 1] += dp[i][j] * j
            dp[i + j - 1][j] += dp[i][j] * (i + 1)
    print(dp[N][1] * X + dp[N][0] * Y)

solve()

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    #N = int(input())
    #A = list(map(int, input().split()))
    #A = [int(input()) for _ in range(N)]
    #S = [input() for _ in range(N)]
    #S = [list(input()) for _

=======
Suggestion 3

def solve(N, X, Y):
    if N == 1:
        return 0
    else:
        return (N-1) * X

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    print((N-1)*X + Y)

main()

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    print((X+Y)*N)

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #dp[i][j] = i番目の宝石をj個の宝石に変換するときの最大値
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            dp[i][j] = max(dp[i][j], dp[i][j+1] + X)
            dp[i][j] = max(dp[i][j], dp[i+1][j] + Y)
    print(dp[0][0])

=======
Suggestion 7

def solve(N, X, Y):
    # WRITE YOUR CODE HERE
    ans = 0
    return ans

=======
Suggestion 8

def solve(N, X, Y):
    return 0

=======
Suggestion 9

def solve(n, x, y):
    return 0
