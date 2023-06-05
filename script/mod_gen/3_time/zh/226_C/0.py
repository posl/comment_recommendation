def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            for j in a[i]:
                dp[i] = max(dp[i], dp[j - 1] + t[i])
    print(max(dp))

if __name__ == '__main__':
    main()