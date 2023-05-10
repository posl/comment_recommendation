def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    N = 10**6 + 1
    fac = [0] * N
    fac[0] = 1
    for i in range(1, N):
        fac[i] = fac[i-1] * i % mod
    inv = [0] * N
    inv[-1] = pow(fac[-1], mod-2, mod)
    for i in range(N-2, -1, -1):
        inv[i] = inv[i+1] * (i+1) % mod
    def comb(n, r):
        if n < r:
            return 0
        return fac[n] * inv[n-r] * inv[r] % mod
    if (x+y) % 3 != 0:
        print(0)
        return
    n = (x+y)//3
    r = x - n
    if r < 0 or r > n:
        print(0)
        return
    print(comb(n, r))

if __name__ == '__main__':
    main()