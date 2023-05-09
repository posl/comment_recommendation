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
                    dp[min(X, i + a)][min(Y, j + b)] = True
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                return i + j
    return -1
print(solve())
