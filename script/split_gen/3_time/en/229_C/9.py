def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    sum = 0
    for i in range(n):
        a[i], b[i] = map(int, input().split())
        sum += a[i] * b[i]
    dp = [0] * (sum+1)
    for i in range(n):
        for j in range(sum, a[i]-1, -1):
            dp[j] = max(dp[j], dp[j-a[i]] + b[i])
    print(min(sum, w, max(dp[:w+1])))
