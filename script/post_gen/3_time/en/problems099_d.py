Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                cost = 0
                for l in range(C):
                    cost += D[l][i] * cnt[0][l]
                    cost += D[l][j] * cnt[1][l]
                    cost += D[l][k] * cnt[2][l]
                ans = min(ans, cost)
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cost[(i + j) % 3][c[i][j] - 1] += 1
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    tmp = 0
                    for l in range(C):
                        tmp += D[l][i] * cost[0][l]
                        tmp += D[l][j] * cost[1][l]
                        tmp += D[l][k] * cost[2][l]
                    ans = min(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            D[i][j] = min(D[i][j], D[i][0] + D[0][j])
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j]] += 1
    ans = 10 ** 18
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, D[i][j] * cnt[0][j] + D[j][k] * cnt[1][k] + D[k][i] * cnt[2][i])
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    def cost(x, y):
        return D[(x + y) % 3][y]

    res = 0
    for i in range(3):
        res += sum(cost(c[j][k] - 1, i) for j in range(N) for k in range(N))

    print(res)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 3色ごとのマスの個数
    count = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            count[(i + j) % 3][c[i][j] - 1] += 1

    # 3色の最小コスト
    cost = [[0] * C for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[j][k] * count[i][k]

    # 3色の最小コストの最小値
    print(min(sum(cost, [])))

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(C)]
    c = [list(map(int, input().split())) for i in range(N)]
    c1 = []
    c2 = []
    c3 = []
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                c1.append(c[i][j])
            elif (i + j) % 3 == 1:
                c2.append(c[i][j])
            else:
                c3.append(c[i][j])
    cost1 = [0] * C
    cost2 = [0] * C
    cost3 = [0] * C
    for i in range(C):
        for j in c1:
            cost1[i] += D[j - 1][i]
        for j in c2:
            cost2[i] += D[j - 1][i]
        for j in c3:
            cost3[i] += D[j - 1][i]
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, cost1[i] + cost2[j] + cost3[k])
    print(ans)

=======
Suggestion 7

def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 3色のコストを求める
    cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cost[(i + j) % 3][c[i][j] - 1] += 1

    # 3色のコストを組み合わせたコストを求める
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += cost[0][l] * D[l][i]
                    tmp += cost[1][l] * D[l][j]
                    tmp += cost[2][l] * D[l][k]
                ans = min(ans, tmp)

    print(ans)

=======
Suggestion 8

def solve():
    N, C = map(int, input().split())
    D = []
    for _ in range(C):
        D.append(list(map(int, input().split())))
    c = []
    for _ in range(N):
        c.append(list(map(int, input().split())))
    mod0 = [[0] * C for _ in range(3)]
    mod1 = [[0] * C for _ in range(3)]
    mod2 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                mod0[c[i][j] - 1][0] += 1
                mod0[c[i][j] - 1][1] += 1
                mod0[c[i][j] - 1][2] += 1
            elif (i + j) % 3 == 1:
                mod1[c[i][j] - 1][0] += 1
                mod1[c[i][j] - 1][1] += 1
                mod1[c[i][j] - 1][2] += 1
            else:
                mod2[c[i][j] - 1][0] += 1
                mod2[c[i][j] - 1][1] += 1
                mod2[c[i][j] - 1][2] += 1
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    tmp = 0
                    for l in range(C):
                        tmp += mod0[l][0] * D[l][i]
                        tmp += mod0[l][1] * D[l][j]
                        tmp += mod0[l][2] * D[l][k]
                        tmp += mod1[l][0] * D[l][j]
                        tmp += mod1[l][1] * D[l][k]
                        tmp += mod1[l][2] * D[l][i]
                        tmp += mod2[l][0] * D[l][k]
                        tmp += mod2[l][1] * D[l][i]
                        tmp += mod2[l][2] *

=======
Suggestion 9

def main():
    from sys import stdin
    from itertools import product
    from collections import defaultdict
    from bisect import bisect_left

    readline = stdin.readline
    N, C = map(int, readline().split())
    D = [list(map(int, readline().split())) for _ in range(C)]
    c = [list(map(int, readline().split())) for _ in range(N)]

    cost = [[0] * C for _ in range(3)]
    for i, j, k in product(range(N), range(N), range(C)):
        cost[(i + j) % 3][k] += D[c[i][j] - 1][k]

    dp = [[float('inf')] * C for _ in range(3)]
    for i in range(C):
        dp[0][i] = cost[0][i]

    for i in range(1, 3):
        for j, k in product(range(C), range(C)):
            if j != k:
                dp[i][k] = min(dp[i][k], dp[i - 1][j] + cost[i][k])

    print(min(dp[2]))

=======
Suggestion 10

def solve(n,c,d,cs):
    #n is the number of rows and columns
    #c is the number of colors
    #d is the cost of changing a color from j to i
    #cs is the initial colors of the grid
    #returns the minimum cost of changing the colors of the grid
    #so that the grid is a good grid
    
    #dp[i][j] is the minimum cost of changing the colors of the grid
    #so that the grid is a good grid
    #and the color of the first i rows is j
    dp = [[float('inf')]*c for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(c):
            for k in range(c):
                if (i+j)%3 != (i+k)%3:
                    dp[i+1][k] = min(dp[i+1][k],dp[i][j]+d[j][k])
    return min(dp[n])
