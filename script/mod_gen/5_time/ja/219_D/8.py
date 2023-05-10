def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k] == 1:
                    dp[min(j+a[i], x)][min(k+b[i], y)] = 1
    ans = 0
    while dp[x-ans][y-ans] == 0:
        ans += 1
        if ans > x or ans > y:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()