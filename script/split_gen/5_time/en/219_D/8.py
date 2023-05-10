def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    dp = [[False for _ in range(Y + 1)] for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y] and x + a <= X and y + b <= Y:
                    dp[x + a][y + b] = True
    for x in range(X, -1, -1):
        for y in range(Y, -1, -1):
            if dp[x][y]:
                print(X + Y - x - y)
                exit()
    print(-1)
