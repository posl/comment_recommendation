def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    def modinv(a, mod):
        b = mod
        u, v = 1, 0
        while b:
            t = a // b
            a -= t * b
            a, b = b, a
            u -= t * v
            u, v = v, u
        u %= mod
        if u < 0:
            u += mod
        return u
    def nCr(n, r, mod):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n-r] % mod
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    for i in range( 2, n + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )
    ans = pow(2, n, mod) - 1 - nCr(n, a, mod) - nCr(n, b, mod)
    print(ans % mod)
