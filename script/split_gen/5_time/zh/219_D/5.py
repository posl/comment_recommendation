def lunchBox():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for a, b in ab:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j] == 1:
                    dp[min(i+a, x)][min(j+b, y)] = 1
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j] == 1:
                return i+j
    return -1
print(lunchBox())
