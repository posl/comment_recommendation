def main():
    num, match = map(int, input().split())
    matchsticks = list(map(int, input().split()))
    matchsticks.sort(reverse=True)
    dp = [-1 for _ in range(num + 1)]
    dp[0] = 0
    for i in range(1, num + 1):
        for j in range(match):
            if i >= matchsticks[j] and dp[i - matchsticks[j]] >= 0:
                dp[i] = max(dp[i], dp[i - matchsticks[j]] + 1)
    if dp[num] == -1:
        print(0)
    else:
        ans = ''
        for i in range(dp[num]):
            for j in range(match):
                if num >= matchsticks[j] and dp[num - matchsticks[j]] == dp[num] - 1:
                    ans += str(matchsticks[j])
                    num -= matchsticks[j]
                    break
        print(ans)

if __name__ == '__main__':
    main()