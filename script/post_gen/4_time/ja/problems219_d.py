Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = -1
    for i in range(N):
        for j in range(N):
            if A[i] + B[j] >= X and A[i] + B[j] >= Y:
                if ans == -1:
                    ans = i + j + 2
                else:
                    ans = min(ans, i + j + 2)
    print(ans)

main()

=======
Suggestion 2

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    dp = [[False for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k] and j+a[i] <= x and k+b[i] <= y:
                    dp[j+a[i]][k+b[i]] = True

    for j in range(x, -1, -1):
        for k in range(y, -1, -1):
            if dp[j][k]:
                print(j+k)
                exit()
    print(-1)

=======
Suggestion 3

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for i in reversed(range(X + 1)):
            for j in reversed(range(Y + 1)):
                if dp[i][j]:
                    dp[min(X, i + a)][min(Y, j + b)] = True

    for i in reversed(range(X + 1)):
        for j in reversed(range(Y + 1)):
            if dp[i][j]:
                return i + j
    return -1

print(solve())

=======
Suggestion 4

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j]:
                    dp[min(X, i + a)][min(Y, j + b)] = True
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                return i + j
    return -1

print(solve())

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True

    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j]:
                    if i+a <= X and j+b <= Y:
                        dp[i+a][j+b] = True

    ans = -1
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                ans = i+j
                break
        if ans > 0:
            break

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0 for _ in range(Y + 1)] for _ in range(X + 1)]
    dp[0][0] = 1
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j] == 0:
                    continue
                if i + a <= X and j + b <= Y:
                    dp[i + a][j + b] = 1

    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j] == 1:
                return print(i + j)
    return print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: (x[0], x[1]))

    dp = [[0 for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = 1
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j] == 0:
                    continue
                if i + a <= X and j + b <= Y:
                    dp[i+a][j+b] = 1

    ans = 0
    for i in range(X+1):
        for j in range(Y+1):
            if dp[i][j] == 1:
                ans = max(ans, i+j)

    if ans == 0:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j][k] := i番目までの弁当でたこ焼きをj個以上、たい焼きをk個以上にするために必要な弁当の最小個数
    dp = [[[float('inf')] * (y + 1) for _ in range(x + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(n):
        a, b = ab[i]
        for j in range(x + 1):
            for k in range(y + 1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                dp[i + 1][min(j + a, x)][min(k + b, y)] = min(dp[i + 1][min(j + a, x)][min(k + b, y)], dp[i][j][k] + 1)

    ans = dp[n][x][y]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()

=======
Suggestion 9

def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    dp = [[False for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = True
    for a, b in ab:
        for i in range(x-a, -1, -1):
            for j in range(y-b, -1, -1):
                if dp[i][j]:
                    dp[i+a][j+b] = True
    ans = float('inf')
    for i in range(x+1):
        for j in range(y+1):
            if dp[i][j]:
                ans = min(ans, i+j)
    print(ans if ans != float('inf') else -1)

=======
Suggestion 10

def solve():
    N = int(input())
    X,Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    INF = 10**18
    dp = [[[INF for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(1,N+1):
        a,b = AB[i-1]
        for j in range(X+1):
            for k in range(Y+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                if j >= a and k >= b:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-a][k-b] + 1)
    if dp[N][X][Y] == INF:
        print(-1)
    else:
        print(dp[N][X][Y])

solve()
