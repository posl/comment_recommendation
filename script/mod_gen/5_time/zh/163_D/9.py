def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    # 从n+1个数中选k个，和的取值范围为[sum1, sum2]
    sum1 = sum([10 ** 100 + i for i in range(k)])
    sum2 = sum([10 ** 100 + i for i in range(n, n - k, -1)])
    # 用前缀和数组存储组合数
    prefix = [1 for i in range(sum2 - sum1 + 1)]
    for i in range(1, sum2 - sum1 + 1):
        prefix[i] = prefix[i - 1] * i % mod
    # 求逆元
    inverse = [1 for i in range(sum2 - sum1 + 1)]
    inverse[-1] = pow(prefix[-1], mod - 2, mod)
    for i in range(sum2 - sum1, 0, -1):
        inverse[i - 1] = inverse[i] * i % mod
    # 求组合数
    def comb(n, k, mod):
        if k == 0:
            return 1
        return prefix[n] * inverse[k] % mod * inverse[n - k] % mod
    print((comb(sum2 - sum1 + 1, k - 1, mod) - comb(sum2 - sum1 + 1, k, mod)) % mod)

if __name__ == '__main__':
    main()