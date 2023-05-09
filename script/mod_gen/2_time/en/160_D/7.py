def main():
    N, X, Y = map(int, input().split())
    G = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i == j:
                continue
            elif j == X:
                G[i][j] = 1
                G[j][i] = 1
            elif j == Y:
                G[i][j] = 1
                G[j][i] = 1
            elif j == i+1:
                G[i][j] = 1
                G[j][i] = 1
            else:
                G[i][j] = 1000
                G[j][i] = 1000
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]
    ans = [0]*(N-1)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if G[i][j] != 1000:
                ans[G[i][j]-1] += 1
    for i in range(N-1):
        print(ans[i])

if __name__ == '__main__':
    main()