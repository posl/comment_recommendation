def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j]:
                    dp[min(i + a, X)][min(j + b, Y)] = True
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)
solve()

if __name__ == '__main__':
    solve()