def problem238_c():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n >= 10 ** i:
            ans += 9 * pow(10, i - 1, mod)
        else:
            ans += (n - 10 ** (i - 1) + 1) * pow(10, i - 1, mod)
            break
    print(ans % mod)
