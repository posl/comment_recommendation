def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * (b[0] + 1)
    for i in range(a[0], b[0] + 1):
        dp[i] = 1
    for i in range(1, n):
        dp_new = [0] * (b[i] + 1)
        for j in range(a[i], b[i] + 1):
            dp_new[j] = sum(dp[:j + 1]) % mod
        dp = dp_new
    print(sum(dp) % mod)
