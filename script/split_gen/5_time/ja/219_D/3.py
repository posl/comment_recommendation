def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False for _ in range(y + 1)] for _ in range(x + 1)]
    dp[0][0] = True
    for a, b in ab:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j]:
                    dp[min(x, i + a)][min(y, j + b)] = True
    for i in range(x + 1):
        for j in range(y + 1):
            if dp[i][j] and i >= x and j >= y:
                print(i + j)
                return
    print(-1)
