def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    # Mの約数を求める
    divisors = []
    for i in range(1, int(M**0.5) + 1):
        if M % i == 0:
            divisors.append(i)
            if M // i != i:
                divisors.append(M // i)
    divisors.sort()
    # print(divisors)
    # 約数の個数を数える
    cnt = [0] * len(divisors)
    for i in range(len(divisors)):
        # 約数の個数を数える
        for j in range(divisors[i], M+1, divisors[i]):
            cnt[i] += 1
    # print(cnt)
    # 逆元を求める
    inv = [1] * (M+1)
    for i in range(2, M+1):
        inv[i] = mod - (mod // i) * inv[mod % i] % mod
    # print(inv)
    # 約数の個数の累積和を求める
    cum_cnt = [0] * (len(divisors)+1)
    for i in range(len(divisors)):
        cum_cnt[i+1] = cum_cnt[i] + cnt[i]
    # print(cum_cnt)
    # 約数の個数の累積和の逆元を求める
    inv_cum_cnt = [0] * (len(divisors)+1)
    for i in range(len(divisors)):
        inv_cum_cnt[i+1] = inv_cum_cnt[i] + inv[cnt[i]]
    # print(inv_cum_cnt)
    # 約数の個数の累積和の逆元を求める
    ans = 0
    for i in range(1, len(divisors)):
        # print(divisors[i], cum_cnt[i], inv_cum_cnt[i])
        ans += divisors[i] * (cum_cnt[i] * inv_cum_cnt[i] % mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()