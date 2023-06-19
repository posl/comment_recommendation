def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for i in range(y+1)] for j in range(x+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j >= a[i] and k >= b[i]:
                    dp[j][k] = dp[j][k] or dp[j-a[i]][k-b[i]]
    if dp[x][y]:
        print(0)
        return
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j >= a[i] and k >= b[i]:
                    dp[j][k] = dp[j][k] or dp[j-a[i]][k-b[i]]
    if dp[x][y]:
        print(1)
        return
    print(-1)

if __name__ == '__main__':
    main()