Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = True
    for a, b in ab:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if i - a >= 0 and j - b >= 0:
                    dp[i][j] |= dp[i - a][j - b]
    ans = float('inf')
    for i in range(x, x + 301):
        for j in range(y, y + 301):
            if dp[i][j]:
                ans = min(ans, i + j)
    print(ans if ans < float('inf') else -1)

=======
Suggestion 2

def get_input():
    n = int(input())
    x,y = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    return n,x,y,a,b

=======
Suggestion 3

def solve():
    N = int(input())
    X, Y = map(int, input().split())

    #dp[i][j][k]表示用前i个便当，j个章鱼烧，k个鱼形蛋糕
    #能否满足条件
    dp = [[[False for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = True

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(X+1):
            for k in range(Y+1):
                if j >= a and k >= b:
                    dp[i+1][j][k] = dp[i][j][k] or dp[i][j-a][k-b]
                else:
                    dp[i+1][j][k] = dp[i][j][k]

    if dp[N][X][Y]:
        print("Yes")
    else:
        print("No")

solve()

=======
Suggestion 4

def solution():
    pass

=======
Suggestion 5

def solve():
    n = int(input())
    x, y = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = True
    for a, b in a_b:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j] and i + a <= x and j + b <= y:
                    dp[i + a][j + b] = True
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)

=======
Suggestion 6

def lunchBox():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for a, b in ab:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j] == 1:
                    dp[min(i+a, x)][min(j+b, y)] = 1
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j] == 1:
                return i+j
    return -1

print(lunchBox())

=======
Suggestion 7

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    dp = [[[0 for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k] == 1:
                    dp[i+1][j][k] = 1
                    if j+a[i] <= x and k+b[i] <= y:
                        dp[i+1][j+a[i]][k+b[i]] = 1
    for i in range(n, -1, -1):
        if dp[i][x][y] == 1:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 8

def solution():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True

    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if i >= a and j >= b:
                    dp[i][j] |= dp[i - a][j - b]

    ans = -1
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                ans = max(ans, i + j)

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_num = 10000000000
    for i in range(n):
        if a[i] >= x and b[i] >= y:
            min_num = min(min_num, a[i] + b[i])
    if min_num == 10000000000:
        print(-1)
    else:
        print(min_num)

=======
Suggestion 10

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    dp = [[0]*(Y+1) for _ in range(X+1)]
    dp[0][0] = 1
    ans = 10**9
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j]:
                    dp[min(X, i+a)][min(Y, j+b)] = 1
                    if i+a >= X and j+b >= Y:
                        ans = min(ans, dp[i][j]+1)
    print(ans if ans != 10**9 else -1)
