def main():
    N, M = map(int, input().split())
    #N, M = 100000, 1000000000
    mod = 10**9+7
    #素因数分解
    p = {}
    i = 2
    while i*i <= M:
        while M%i == 0:
            if i in p:
                p[i] += 1
            else:
                p[i] = 1
            M //= i
        i += 1
    if M != 1:
        p[M] = 1
    #print(p)
    # 素因数ごとに考える
    ans = 1
    for k, v in p.items():
        ans *= comb(N+v-1, N-1, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()