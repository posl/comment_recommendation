def solve():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        if k[i] > 0:
            a[i] = list(map(int, input().split()))
            for j in range(k[i]):
                a[i][j] -= 1
    # print(t)
    # print(k)
    # print(a)
    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = max([dp[j] for j in a[i]]) + t[i]
    # print(dp)
    print(dp[n - 1])
    return 0

if __name__ == '__main__':
    solve()