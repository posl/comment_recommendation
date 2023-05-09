def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    D[i][j] = float("inf")
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    dp = [[[0] * C for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(C):
                dp[(i + j) % 3][c[i][j]][k] += D[c[i][j]][k]
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, dp[0][i][j] + dp[1][j][k] + dp[2][k][i])
    print(ans)

if __name__ == '__main__':
    main()