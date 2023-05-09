def main():
    n, k = map(int, input().split())
    l = []
    r = []
    for i in range(k):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    #print(n, k, l, r)
    mod = 998244353
    dp = [0] * (n+1)
    dp[1] = 1
    dpsum = [0] * (n+1)
    dpsum[1] = 1
    for i in range(2, n+1):
        for j in range(k):
            li = i - r[j]
            ri = i - l[j]
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li-1]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    #print(dp)
    print(dp[n])

if __name__ == '__main__':
    main()