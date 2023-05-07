def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    for m in range(N):
                        for n in range(N):
                            for o in range(N):
                                for p in range(N):
                                    for q in range(N):
                                        for r in range(N):
                                            for s in range(N):
                                                for t in range(N):
                                                    for u in range(N):
                                                        for v in range(N):
                                                            for w in range(N):
                                                                for x in range(N):
                                                                    for y in range(N):
                                                                        for z in range(N):
                                                                            if i != j and j != k and k != l and l != m and m != n and n != o and o != p and p != q and q != r and r != s and s != t and t != u and u != v and v != w and w != x and x != y and y != z and z != i and i != 0 and j != 0 and k != 0 and l != 0 and m != 0 and n != 0 and o != 0 and p != 0 and q != 0 and r != 0 and s != 0 and t != 0 and u != 0 and v != 0 and w != 0 and x != 0 and y != 0 and z != 0:
                                                                                if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] + T[p][q] + T[q][r] + T[r][s] + T[s][t] + T[t][u] + T[u][v] + T[v][w] + T[w][x] + T[x][y] + T[y][z] + T[z][i] == K:
                                                                                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()