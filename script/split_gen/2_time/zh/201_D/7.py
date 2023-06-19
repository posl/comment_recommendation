def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if (i+j)%2 == 0:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                if a[i][j] == '+':
                    dp[i][j] += 1
                else:
                    dp[i][j] -= 1
            else:
                dp[i][j] = min(dp[i+1][j],dp[i][j+1])
                if a[i][j] == '+':
                    dp[i][j] -= 1
                else:
                    dp[i][j] += 1
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] == 0:
        print("Draw")
    else:
        print("Aoki")
