def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for i in reversed(range(X + 1)):
            for j in reversed(range(Y + 1)):
                if dp[i][j]:
                    dp[min(X, i + a)][min(Y, j + b)] = True
    for i in range(1, N + 1):
        if dp[min(X, i * AB[i - 1][0])][min(Y, i * AB[i - 1][1])]:
            print(i)
            break
    else:
        print(-1)
