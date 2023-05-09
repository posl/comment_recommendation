def main():
    import sys
    readline = sys.stdin.buffer.readline
    N, S = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(N)]
    #print(N, S)
    #print(AB)
    #dp[i][s] = i枚目までのカードを見て、表をs枚選んだときの、裏の枚数の最小値
    #dp[i][s] = min(dp[i-1][s], dp[i-1][s-1]+1)
    #dp[i][s] = min(dp[i-1][s], dp[i-1][s-a[i]]+1)
    dp = [[float("inf")] * (S+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for s in range(S+1):
            if s >= a:
                dp[i+1][s] = min(dp[i][s], dp[i][s-a]+b)
            else:
                dp[i+1][s] = dp[i][s]
    #print(dp)
    if dp[N][S] == float("inf"):
        print("No")
    else:
        print("Yes")
        ans = []
        s = S
        for i in range(N-1, -1, -1):
            a, b = AB[i]
            if s >= a and dp[i][s-a] + b == dp[i+1][s]:
                ans.append("T")
                s -= a
            else:
                ans.append("H")
        print("".join(ans[::-1]))

if __name__ == '__main__':
    main()