def main():
    s = input()
    n = len(s)
    # dp[i] 表示前i个字符构成的数字除以2019的余数
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * 10 + int(s[i - 1])) % 2019
    # print(dp)
    cnt = [0] * 2019
    for i in range(n + 1):
        cnt[dp[i]] += 1
    # print(cnt)
    ans = 0
    for i in range(2019):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
