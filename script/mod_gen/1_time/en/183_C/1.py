def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(2, N):
            for k in range(3, N):
                for l in range(4, N):
                    for m in range(5, N):
                        for n in range(6, N):
                            for o in range(7, N):
                                for p in range(8, N):
                                    if T[0][i] + T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][o] + T[o][p] == K:
                                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()