def solve():
    S = input()
    S = S[::-1]
    ans = 0
    mod = 10**9 + 7
    for i, s in enumerate(S):
        ans = (ans + (int(s) * pow(10, i, mod)) * (i + 1)) % mod
    print(ans)
