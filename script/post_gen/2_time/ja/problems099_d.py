Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0, 0, 0] for _ in range(C)]
    for i in range(N):
        for j in range(N):
            cost[(c[i][j] - 1)][(i + j) % 3] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, D[i][j] * cost[j][0] + D[j][k] * cost[k][1] + D[k][i] * cost[i][2])
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                D[j][k] = min(D[j][k], D[j][i] + D[i][k])
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(N):
                    for m in range(N):
                        if (l + m) % 3 == 0:
                            tmp += D[c[l][m] - 1][i]
                        elif (l + m) % 3 == 1:
                            tmp += D[c[l][m] - 1][j]
                        else:
                            tmp += D[c[l][m] - 1][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    mod = 3
    cnt = [[0]*C for _ in range(mod)]
    for i in range(N):
        for j in range(N):
            cnt[(i+j)%mod][c[i][j]-1] += 1
    ans = 10**9
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(mod):
                    tmp += D[i][l]*cnt[l][j]
                    tmp += D[j][l]*cnt[l][k]
                    tmp += D[k][l]*cnt[l][i]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # print(c)
    # print(D)
    # print(N, C)
    # print(c)
    # print(D)
    # r = [[0]*C for _ in range(3)]
    # g = [[0]*C for _ in range(3)]
    # b = [[0]*C for _ in range(3)]
    # for i in range(N):
    #     for j in range(N):
    #         if (i+j) % 3 == 0:
    #             r[c[i][j]-1][0] += D[c[i][j]-1][0]
    #             r[c[i][j]-1][1] += D[c[i][j]-1][1]
    #             r[c[i][j]-1][2] += D[c[i][j]-1][2]
    #         elif (i+j) % 3 == 1:
    #             g[c[i][j]-1][0] += D[c[i][j]-1][0]
    #             g[c[i][j]-1][1] += D[c[i][j]-1][1]
    #             g[c[i][j]-1][2] += D[c[i][j]-1][2]
    #         elif (i+j) % 3 == 2:
    #             b[c[i][j]-1][0] += D[c[i][j]-1][0]
    #             b[c[i][j]-1][1] += D[c[i][j]-1][1]
    #             b[c[i][j]-1][2] += D[c[i][j]-1][2]
    # print(r)
    # print(g)
    # print(b)
    # r_min = 10000000000000000000
    # g_min = 10000000000000000000
    # b_min = 10000000000000000000
    # for i in range(C):
    #     for j in range(C):
    #         for k in range(C):
    #             if i != j and i != k and j != k:

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    c = [[c[i][j] - 1 for j in range(N)] for i in range(N)]

    cost = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(C):
                cost[(i + j) % 3][k] += D[c[i][j]][k]

    ans = 10 ** 10
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
    count = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            count[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * count[0][l]
                    tmp += D[l][j] * count[1][l]
                    tmp += D[l][k] * count[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 7

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    C1 = [[0] * C for _ in range(3)]
    C2 = [[0] * C for _ in range(3)]
    C3 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1[c[i][j] - 1][0] += 1
                C2[c[i][j] - 1][1] += 1
                C3[c[i][j] - 1][2] += 1
            elif (i + j) % 3 == 1:
                C1[c[i][j] - 1][1] += 1
                C2[c[i][j] - 1][2] += 1
                C3[c[i][j] - 1][0] += 1
            else:
                C1[c[i][j] - 1][2] += 1
                C2[c[i][j] - 1][0] += 1
                C3[c[i][j] - 1][1] += 1
    for i in range(C):
        for j in range(3):
            for k in range(C):
                D[j][i] += D[k][i] * C1[k][j]
    for i in range(C):
        for j in range(3):
            for k in range(C):
                D[j][i] += D[k][i] * C2[k][j]
    for i in range(C):
        for j in range(3):
            for k in range(C):
                D[j][i] += D[k][i] * C3[k][j]
    print(min(D[0]))

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(C)]
    c = [list(map(int, input().split())) for i in range(N)]
    dp = [[0] * C for i in range(3)]
    for i in range(N):
        for j in range(N):
            dp[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += dp[0][l] * D[l][i]
                    tmp += dp[1][l] * D[l][j]
                    tmp += dp[2][l] * D[l][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] -= 1

    # 余りごとに色ごとの個数を数える
    mod = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3][C[i][j]] += 1

    # 余りごとに色を変えるコストを求める
    cost = [[0] * C for _ in range(3)]
    for i in range(3):
        for j in range(C):
            for k in range(C):
                cost[i][j] += D[j][k] * mod[i][k]

    # 余りごとに最小のコストを求める
    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])

    print(ans)

=======
Suggestion 10

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]

    # 3色でグループ分け
    C1 = []
    C2 = []
    C3 = []
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1.append(C[i][j])
            elif (i + j) % 3 == 1:
                C2.append(C[i][j])
            else:
                C3.append(C[i][j])

    # 3色でグループ分けしたものを、色ごとにグループ分け
    C1_1 = []
    C1_2 = []
    C1_3 = []
    C2_1 = []
    C2_2 = []
    C2_3 = []
    C3_1 = []
    C3_2 = []
    C3_3 = []
    for i in range(len(C1)):
        if C1[i] == 1:
            C1_1.append(i)
        elif C1[i] == 2:
            C1_2.append(i)
        else:
            C1_3.append(i)
    for i in range(len(C2)):
        if C2[i] == 1:
            C2_1.append(i)
        elif C2[i] == 2:
            C2_2.append(i)
        else:
            C2_3.append(i)
    for i in range(len(C3)):
        if C3[i] == 1:
            C3_1.append(i)
        elif C3[i] == 2:
            C3_2.append(i)
        else:
            C3_3.append(i)

    # 3色でグループ分けしたものを、色ごとにグループ分けしたものを、色ごとにグループ分け
    C1_1_1 = []
    C1_1_2 = []
    C1_1_3 = []
    C1_2_1 = []
    C1_2_2 = []
    C1
