def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    def cmb(n, r, mod):
        x, y = 1, 1
        for i in range(r):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod
    ans = (ans - cmb(n, a, mod) - cmb(n, b, mod)) % mod
    print(ans)
