def main():
    H, W, A, B = map(int, input().split())
    mod = 10**9 + 7
    fact = [1] * (H+W+1)
    for i in range(1, H+W+1):
        fact[i] = (fact[i-1] * i) % mod
    inv = [1] * (H+W+1)
    inv[-1] = pow(fact[-1], mod-2, mod)
    for i in range(H+W-1, -1, -1):
        inv[i] = (inv[i+1] * (i+1)) % mod
    def comb(n, r):
        return (fact[n] * inv[r] * inv[n-r]) % mod
    ans = 0
    for i in range(W-B):
        ans = (ans + comb(H-A-1+B+i, i) * comb(A-1+W-B-i, A-1)) % mod
    print(ans)
main()

if __name__ == '__main__':
    main()