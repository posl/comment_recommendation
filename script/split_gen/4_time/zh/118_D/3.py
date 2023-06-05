def main():
    n = int(input())
    a = list(map(int, input().split()))
    nums = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(len(a)):
            if i + nums[a[j] - 1] <= n:
                dp[i + nums[a[j] - 1]] = max(dp[i + nums[a[j] - 1]], dp[i] * 10 + a[j])
    print(dp[n])
