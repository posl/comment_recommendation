def main():
    n = int(input())
    a = []
    for i in range(n):
        t, x, a_ = map(int, input().split())
        a.append((t, x, a_))
    a.sort()
    dp = [0] * 5
    for t, x, a_ in a:
        if x == 0:
            dp[0] = max(dp[0], dp[0] + a_)
        elif x == 1:
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
        elif x == 2:
            dp[2] = max(dp[2], dp[1] + a_)
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
        elif x == 3:
            dp[3] = max(dp[3], dp[2] + a_)
            dp[2] = max(dp[2], dp[1] + a_)
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
        else:
            dp[4] = max(dp[4], dp[3] + a_)
            dp[3] = max(dp[3], dp[2] + a_)
            dp[2] = max(dp[2], dp[1] + a_)
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
    print(max(dp))

if __name__ == '__main__':
    main()