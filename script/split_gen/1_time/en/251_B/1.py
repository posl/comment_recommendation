def solve():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (w + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(w, -1, -1):
            if dp[j] == 1:
                if j + a[i] <= w:
                    dp[j + a[i]] = 1
    print(sum(dp))
