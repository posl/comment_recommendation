def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False]*(n+1)
    for i in range(n+1):
        for j in range(k):
            if i-a[j] >= 0 and dp[i-a[j]] == False:
                dp[i] = True
    ans = 0
    for i in range(n+1):
        if dp[i] == False:
            ans += 1
    print(ans)
