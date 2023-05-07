def main():
    N, M = map(int, input().split())
    # Mの素因数分解
    f = {}
    i = 2
    while i * i <= M:
        while M % i == 0:
            M //= i
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        i += 1
    if M > 1:
        if M in f:
            f[M] += 1
        else:
            f[M] = 1
    #print(f)
    # 素因数分解の結果を用いてN個の数の組み合わせを求める
    ans = 1
    mod = 10**9 + 7
    for x in f.values():
        ans *= cmb(N-1+x, x, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()