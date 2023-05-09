def solve():
    H, W, A, B = map(int, input().split())
    mod = 10**9+7
    n = H+W
    kaijou = [1]
    for i in range(1, n+1):
        kaijou.append(kaijou[-1]*i%mod)
    kaijou_inv = [0]*(n+1)
    kaijou_inv[n] = pow(kaijou[n], mod-2, mod)
    for i in range(n, 0, -1):
        kaijou_inv[i-1] = kaijou_inv[i]*i%mod
    def cmb(n, r):
        if n < r:
            return 0
        else:
            return kaijou[n]*kaijou_inv[r]*kaijou_inv[n-r]%mod
    ans = 0
    for i in range(B, W):
        ans += cmb(i+A-1, i)*cmb(W-i+H-A-2, H-A-1)%mod
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()