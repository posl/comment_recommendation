def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = True
    for a, b in ab:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if i - a >= 0 and j - b >= 0:
                    dp[i][j] |= dp[i - a][j - b]
    ans = float('inf')
    for i in range(x, x + 301):
        for j in range(y, y + 301):
            if dp[i][j]:
                ans = min(ans, i + j)
    print(ans if ans < float('inf') else -1)

if __name__ == '__main__':
    main()