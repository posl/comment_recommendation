Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True
    for a, b in AB:
        for x in range(X-a, -1, -1):
            for y in range(Y-b, -1, -1):
                if dp[x][y]:
                    dp[x+a][y+b] = True
    ans = -1
    for x in range(X+1):
        for y in range(Y+1):
            if dp[x][y]:
                if ans == -1:
                    ans = x+y
                else:
                    ans = min(ans, x+y)
    print(ans)

=======
Suggestion 2

def main():
    # input
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # compute
    ans = float('inf')
    for i in range(2**N):
        cnt_t = 0
        cnt_y = 0
        cnt = 0
        for j in range(N):
            if (i >> j) & 1:
                cnt_t += AB[j][0]
                cnt_y += AB[j][1]
                cnt += 1
        if cnt_t >= X and cnt_y >= Y:
            ans = min(ans, cnt)

    # output
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # dp[i][j][k] := i 番目までの弁当を使って、たこ焼きを j 個以上、たい焼きを k 個以上手に入れるために必要な弁当の個数の最小値
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0

    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                dp[i+1][min(j+a[i], x)][min(k+b[i], y)] = min(dp[i+1][min(j+a[i], x)][min(k+b[i], y)], dp[i][j][k] + 1)
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])

=======
Suggestion 4

def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    dp = [[False for _ in range(y + 1)] for _ in range(x + 1)]
    dp[0][0] = True
    for a, b in ab:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j]:
                    dp[min(x, i + a)][min(y, j + b)] = True
    for i in range(x + 1):
        for j in range(y + 1):
            if dp[i][j] and i >= x and j >= y:
                print(i + j)
                return
    print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: (x[0] + x[1], x[0]), reverse=True)
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if i + a <= X and j + b <= Y:
                    dp[i + a][j + b] = max(dp[i + a][j + b], dp[i][j] + 1)
    print(dp[X][Y] if dp[X][Y] else -1)

=======
Suggestion 6

def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    dp = [[[False for k in range(y + 1)] for j in range(x + 1)] for i in range(n + 1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(x + 1):
            for k in range(y + 1):
                if dp[i][j][k]:
                    dp[i + 1][j][k] = True
                    if j + ab[i][0] <= x and k + ab[i][1] <= y:
                        dp[i + 1][j + ab[i][0]][k + ab[i][1]] = True
    ans = -1
    for i in range(n + 1):
        if dp[i][x][y]:
            ans = i
            break
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = -1
    for i in range(n):
        if a[i] >= x and b[i] >= y:
            ans = 1
            break
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[j + A[i]][k + B[i]] = max(dp[j + A[i]][k + B[i]], dp[j][k] + 1)

    if dp[X][Y] == 0:
        print(-1)
    else:
        print(dp[X][Y])

=======
Suggestion 9

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k] == 1:
                    dp[min(j+a[i], x)][min(k+b[i], y)] = 1
    ans = 0
    while dp[x-ans][y-ans] == 0:
        ans += 1
        if ans > x or ans > y:
            print(-1)
            return
    print(ans)

=======
Suggestion 10

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
                    dp[min(i + a, X)][min(j + b, Y)] = True
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)

solve()
