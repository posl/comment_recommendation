Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w, a, b = map(int, input().split())
    dp = [[0] * (1 << w) for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(1 << w):
            dp[i + 1][j] += dp[i][j >> 1]
            if j & 1 == 0 and j & 2 == 0 and (j & 1 << (w - 1)) == 0:
                dp[i][j | 3] += dp[i][j]
            if j & 1 == 0 and (j & 1 << (w - 1)) == 0 and a > 0:
                dp[i][j | 1 | 1 << (w - 1)] += dp[i][j]
            if j & 1 == 0 and b > 0:
                dp[i][j | 1] += dp[i][j]
            if j & 1 << (w - 1) == 0 and b > 0:
                dp[i][j | 1 << (w - 1)] += dp[i][j]
    print(dp[h][0])

=======
Suggestion 2

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)

=======
Suggestion 3

def solve():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            count = 0
            for k in range(H):
                for l in range(W):
                    if (i>>k)&1 == 0 and (j>>l)&1 == 0:
                        count += 1
            if count == A:
                ans += 1
    print(ans)

=======
Suggestion 4

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

=======
Suggestion 5

def calc_combination(a, b):
    if b == 0 or a == b:
        return 1
    else:
        return calc_combination(a - 1, b - 1) + calc_combination(a - 1, b)

=======
Suggestion 6

def main():
    H,W,A,B = map(int,input().split())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            a = bin(i).count("1")
            b = bin(j).count("1")
            if a==A and b==B:
                ans += 1
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def solve():
    H,W,A,B = map(int,input().split())
    print(H,W,A,B)
    print("hello")
