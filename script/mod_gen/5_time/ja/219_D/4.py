def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: (x[0] + x[1], x[0]), reverse=True)
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if i + a <= X and j + b <= Y:
                    dp[i + a][j + b] = max(dp[i + a][j + b], dp[i][j] + 1)
    print(dp[X][Y] if dp[X][Y] else -1)

if __name__ == '__main__':
    main()