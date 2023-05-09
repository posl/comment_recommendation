def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(C)]
    c = [list(map(int, input().split())) for i in range(N)]
    dp = [[0] * C for i in range(3)]
    for i in range(N):
        for j in range(N):
            dp[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += dp[0][l] * D[l][i]
                    tmp += dp[1][l] * D[l][j]
                    tmp += dp[2][l] * D[l][k]
                ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()