def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = t[i] + max(dp[j - 1] for j in a[i])
    print(dp[n - 1])

if __name__ == '__main__':
    main()