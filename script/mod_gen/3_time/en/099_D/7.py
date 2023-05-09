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

if __name__ == '__main__':
    solve()