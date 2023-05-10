def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[False for j in range(y+1)] for i in range(x+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k]:
                    dp[min(j+a[i], x)][min(k+b[i], y)] = True
    for i in range(min(x, y)+1):
        if dp[i][i]:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()