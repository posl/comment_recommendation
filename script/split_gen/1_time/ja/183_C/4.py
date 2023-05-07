def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for m in range(l+1, N):
                        for n in range(m+1, N):
                            for o in range(n+1, N):
                                ans += (T[0][i] + T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][0] == K)
    print(ans)
