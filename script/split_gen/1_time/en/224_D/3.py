def main():
    M = int(input())
    E = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    G = [[] for _ in range(9)]
    for u, v in E:
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    for i in range(9):
        G[i].sort()
    P = [i - 1 for i in P]
    ans = 10 ** 9
    for i in range(9):
        for j in range(len(G[i])):
            if P[i] == G[i][j]:
                continue
            G[i][j], P[i] = P[i], G[i][j]
            if P == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                ans = min(ans, 1)
            for k in range(len(G[j])):
                if P[j] == G[j][k]:
                    continue
                G[j][k], P[j] = P[j], G[j][k]
                if P == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    ans = min(ans, 2)
                for l in range(len(G[k])):
                    if P[k] == G[k][l]:
                        continue
                    G[k][l], P[k] = P[k], G[k][l]
                    if P == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                        ans = min(ans, 3)
                    for m in range(len(G[l])):
                        if P[l] == G[l][m]:
                            continue
                        G[l][m], P[l] = P[l], G[l][m]
                        if P == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                            ans = min(ans, 4)
                        for n in range(len(G[m])):
                            if P[m] == G[m][n]:
                                continue
                            G[m][n], P[m] = P[m], G[m][n]
                            if P == [0, 1
