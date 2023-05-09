Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # mod3ごとに色を分類
    color = [[], [], []]
    for i in range(N):
        for j in range(N):
            color[(i+j) % 3].append(c[i][j]-1)

    # 色の組み合わせごとにそれぞれの色に塗り替えるときのコストを求める
    cost = [[0]*C for _ in range(C)]
    for i in range(C):
        for j in range(C):
            for k in color[0]:
                cost[i][j] += D[k][i]
            for k in color[1]:
                cost[i][j] += D[k][j]
            for k in color[2]:
                cost[i][j] += D[k][j]

    # 3色をそれぞれで塗り替えたときの最小コストを求める
    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, cost[i][j]+cost[j][k]+cost[k][i])

    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    c1 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            c1[(i + j) % 3][c[i][j] - 1] += 1

    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for x in range(C):
                    tmp += D[x][i] * c1[0][x]
                for x in range(C):
                    tmp += D[x][j] * c1[1][x]
                for x in range(C):
                    tmp += D[x][k] * c1[2][x]
                ans = min(ans, tmp)

    print(ans)

=======
Suggestion 3

def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    color = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1

    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i==j: continue
            for k in range(C):
                if i==k or j==k: continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*color[0][l]
                    tmp += D[l][j]*color[1][l]
                    tmp += D[l][k]*color[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]

    s = [[0] * c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            s[(i + j) % 3][c[i][j] - 1] += 1

    ans = float('inf')
    for i in range(c):
        for j in range(c):
            if i == j:
                continue
            for k in range(c):
                if i == k or j == k:
                    continue
                cost = 0
                for l in range(c):
                    cost += s[0][l] * d[l][i]
                    cost += s[1][l] * d[l][j]
                    cost += s[2][l] * d[l][k]
                ans = min(ans, cost)
    print(ans)

=======
Suggestion 5

def main():
    N,C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    color = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1
    ans = 10**9
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*color[0][l]
                    tmp += D[l][j]*color[1][l]
                    tmp += D[l][k]*color[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    D = [[int(i) for i in input().split()] for _ in range(C)]
    c = [[int(i) for i in input().split()] for _ in range(N)]
    print(D)
    print(c)

=======
Suggestion 7

def main():
    n,c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    cc = [list(map(int, input().split())) for _ in range(n)]
    cc0 = [[0 for _ in range(c)] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            cc0[(i+j)%3][cc[i][j]-1] += 1
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            if i==j:
                continue
            for k in range(c):
                if i==k or j==k:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += cc0[0][l]*d[l][i]
                    tmp += cc0[1][l]*d[l][j]
                    tmp += cc0[2][l]*d[l][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 8

def solve():
    N,C = map(int,input().split())
    D = [list(map(int,input().split())) for i in range(C)]
    c = [list(map(int,input().split())) for i in range(N)]
    mod = [[0]*C for i in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3][c[i][j]-1] += 1
    ans = 100000000
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*mod[0][l]
                    tmp += D[l][j]*mod[1][l]
                    tmp += D[l][k]*mod[2][l]
                ans = min(ans,tmp)
    print(ans)

=======
Suggestion 9

def wrongness(D, c, N, C):
    w = 0
    for i in range(N):
        for j in range(N):
            if (i+j) % 3 == 0:
                w += D[c[i][j]-1][0]
            elif (i+j) % 3 == 1:
                w += D[c[i][j]-1][1]
            else:
                w += D[c[i][j]-1][2]
    return w

=======
Suggestion 10

def get_min_wrongness(c, d, n):
    wrongness = 0
    for i in range(n):
        for j in range(n):
            if (i+j) % 3 == 0:
                wrongness += d[c[i][j]-1][0]
            elif (i+j) % 3 == 1:
                wrongness += d[c[i][j]-1][1]
            elif (i+j) % 3 == 2:
                wrongness += d[c[i][j]-1][2]
    return wrongness
