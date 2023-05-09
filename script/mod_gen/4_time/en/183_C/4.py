def solve():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(i + 1, N):
            T[i][j] += T[j][i]
            T[j][i] = T[i][j]
    for i in range(1, N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        for n in range(m + 1, N):
                            if T[0][i] + T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][n] + T[n][0] == K:
                                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()