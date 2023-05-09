def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i == X and j == Y:
                G[i][j] = 1
                G[j][i] = 1
                continue
            if i == Y and j == X:
                G[i][j] = 1
                G[j][i] = 1
                continue
            if i + 1 == j:
                G[i][j] = 1
                G[j][i] = 1
                continue
            if j + 1 == i:
                G[i][j] = 1
                G[j][i] = 1
                continue
    for k in range(1, N):
        ans = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if G[i][j] == k:
                    ans += 1
        print(ans)

if __name__ == '__main__':
    main()