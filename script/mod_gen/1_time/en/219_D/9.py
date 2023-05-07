def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if j + a <= X and k + b <= Y:
                    dp[j + a][k + b] = min(dp[j + a][k + b], dp[j][k] + 1)
    ans = dp[X][Y]
    if ans == float('inf'):
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()