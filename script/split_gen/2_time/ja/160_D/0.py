def main():
    N, X, Y = map(int, input().split())
    G = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        G[i][i + 1] = 1
        G[i + 1][i] = 1
    G[X - 1][Y - 1] = 1
    G[Y - 1][X - 1] = 1
    for k in range(1, N):
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                if G[i][j] == k:
                    ans += 1
        print(ans)
