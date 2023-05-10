def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10 ** 9
    D = [[INF] * N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for a, b, c in ABC:
        D[a - 1][b - 1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if D[s][t] == D[s][k] + D[k][t]:
                    ans += D[s][t]
                    break
    print(ans)

if __name__ == '__main__':
    main()