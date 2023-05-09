def main():
    N = int(input())
    holes = [[],[],[],[],[]]
    for _ in range(N):
        t,x,a = map(int, input().split())
        holes[x].append((t,a))
    for i in range(5):
        holes[i].sort()
    dp = [[0,0,0,0,0] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(5):
            dp[i][j] = dp[i-1][j]
            if holes[j] and holes[j][0][0] == i:
                a = holes[j][0][1]
                holes[j].pop(0)
                for k in range(5):
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+a)
    print(max(dp[N]))

if __name__ == '__main__':
    main()