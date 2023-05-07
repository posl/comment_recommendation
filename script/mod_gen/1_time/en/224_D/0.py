def main():
    M = int(input())
    G = [[0] * 9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1][v - 1] = 1
        G[v - 1][u - 1] = 1
    p = list(map(int, input().split()))
    p = [x - 1 for x in p]
    ans = -1
    for i in range(9):
        for j in range(9):
            if i != j and G[i][j] == 1:
                G[i][j] = 0
                G[j][i] = 0
                for k in range(9):
                    if k != i and k != j and G[i][k] == 1 and G[j][k] == 1:
                        G[i][k] = 0
                        G[k][i] = 0
                        G[j][k] = 0
                        G[k][j] = 0
                        for l in range(9):
                            if l != i and l != j and l != k and G[i][l] == 1 and G[j][l] == 1 and G[k][l] == 1:
                                G[i][l] = 0
                                G[l][i] = 0
                                G[j][l] = 0
                                G[l][j] = 0
                                G[k][l] = 0
                                G[l][k] = 0
                                for m in range(9):
                                    if m != i and m != j and m != k and m != l and G[i][m] == 1 and G[j][m] == 1 and G[k][m] == 1 and G[l][m] == 1:
                                        G[i][m] = 0
                                        G[m][i] = 0
                                        G[j][m] = 0
                                        G[m][j] = 0
                                        G[k][m] = 0
                                        G[m][k] = 0
                                        G[l][m] = 0
                                        G[m][l] = 0
                                        for n in range(9):
                                            if n != i and n != j

if __name__ == '__main__':
    main()