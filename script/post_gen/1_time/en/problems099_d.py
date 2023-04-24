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
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * cnt[0][l]
                    tmp += D[l][j] * cnt[1][l]
                    tmp += D[l][k] * cnt[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    C1, C2, C3 = [], [], []
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1.append(c[i][j])
            elif (i + j) % 3 == 1:
                C2.append(c[i][j])
            else:
                C3.append(c[i][j])
    D1, D2, D3 = [0]*C, [0]*C, [0]*C
    for i in range(C):
        for j in range(C):
            D1[i] += D[i][j]*C1.count(j+1)
            D2[i] += D[i][j]*C2.count(j+1)
            D3[i] += D[i][j]*C3.count(j+1)
    ans = 10**10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, D1[i] + D2[j] + D3[k])
    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 3色で塗り分ける場合のコストを計算
    cost = [[0] * 3 for _ in range(C)]
    for i in range(N):
        for j in range(N):
            cost[c[i][j] - 1][(i + j) % 3] += 1
    # 3色で塗り分けたときのコストを計算
    dp = [[float("inf")] * C for _ in range(3)]
    for i in range(C):
        dp[0][i] = D[i][0] * cost[i][0]
    for i in range(1, 3):
        for j in range(C):
            for k in range(C):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + D[j][i] * cost[j][i])
    print(min(dp[2]))

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    mod = [0, 0, 0]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3] += 1
    cost = [[0] * C for _ in range(3)]
    for i in range(C):
        for j in range(C):
            cost[0][i] += mod[0] * D[i][j]
            cost[1][i] += mod[1] * D[i][j]
            cost[2][i] += mod[2] * D[i][j]
    for k in range(C):
        for i in range(3):
            for j in range(C):
                cost[i][j] -= D[k][j] * mod[(i + k) % 3]
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 3色のリストを作る
    color = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1

    # 3色のリストを3色のコストにする
    cost = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[k][j] * color[i][k]

    # 3色のコストを全探索する
    ans = 10**9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            c[i][j] -= 1

    # print(N, C)
    # print(D)
    # print(c)

    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9

    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9

    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9

    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9

    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9

    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9

    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9

    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9

    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9

    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9

    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9

    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9

    # 1, 2, 3
    #

=======
Suggestion 7

def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    D[i][j] = 10**9
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    dp = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(C):
                dp[(i+j)%3][k] += D[c[i][j]][k]
    ans = 10**9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, dp[0][i]+dp[1][j]+dp[2][k])
    print(ans)

=======
Suggestion 8

def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if i == k or j == k:
                    continue
                cost = [[0] * C for _ in range(3)]
                for x in range(N):
                    for y in range(N):
                        cost[(x + y) % 3][c[x][y] - 1] += D[c[x][y] - 1][(i + j + k) % C]
                ans = min(ans, sum(min(cost[i]) for i in range(3)))
    print(ans)

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(C)]
    c = [list(map(int, input().split())) for i in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                D[j][k] = min(D[j][k], D[j][i] + D[i][k])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += D[(i + j) % 3][c[i][j] - 1]
    print(ans)

=======
Suggestion 10

def main():
    N, C = map(int, input().split())
    D = [[int(i) for i in input().split()] for _ in range(C)]
    c = [[int(i) for i in input().split()] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    C = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            C[(i + j) % 3][c[i][j]] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * C[0][l]
                    tmp += D[l][j] * C[1][l]
                    tmp += D[l][k] * C[2][l]
                ans = min(ans, tmp)
    print(ans)
