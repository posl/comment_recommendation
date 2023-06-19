def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(1)
        return
    dp = [False] * (n + 1)
    for i in range(n + 1):
        for j in range(k):
            if i - a[j] >= 0:
                dp[i] |= not dp[i - a[j]]
    for i in range(n, 0, -1):
        if not dp[i]:
            print(i)
            return
