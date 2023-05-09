def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    INF = 10**18
    D = [[INF] * N for _ in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        D[a-1][b-1] = c
    for i in range(N):
        D[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if D[i][j] == D[i][k] + D[k][j]:
                    ans += D[i][j]
                    break
    print(ans)

if __name__ == '__main__':
    main()