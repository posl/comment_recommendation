def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    dp = [0 for i in range(w + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(w + 1):
            if j >= a[i]:
                dp[j] += dp[j - a[i]]
    print(dp[w])
