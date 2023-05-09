def main():
    N, M = map(int, input().split())
    f = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            if i == j:
                f[i][j] = 0
            else:
                f[i][j] = 10 ** 12
    for _ in range(M):
        a, b, c = map(int, input().split())
        f[a][b] = c
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if f[i][j] == f[i][k] + f[k][j]:
                    ans += f[i][k]
                    break
    print(ans)
main()
