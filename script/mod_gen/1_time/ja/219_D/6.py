def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a.append(0)
        b.append(0)
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    dp = [[0 for i in range(x+1)] for j in range(y+1)]
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j - a[i] >= 0 and k - b[i] >= 0:
                    dp[j][k] = max(dp[j][k], dp[j-a[i]][k-b[i]] + 1)
    #print(dp)
    if dp[x][y] > 0:
        print(n - dp[x][y])
    else:
        print(-1)

if __name__ == '__main__':
    main()