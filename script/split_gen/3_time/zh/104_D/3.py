def main():
    S = input()
    Q = S.count('?')
    mod = 10**9 + 7
    ans = 0
    for i, s in enumerate(S):
        if s == 'A':
            a = pow(3, Q, mod)
            b = pow(3, i, mod)
            ans += a * b
            ans %= mod
        elif s == 'B':
            a = pow(3, Q, mod)
            b = pow(3, i, mod)
            ans += a * b
            ans %= mod
            ans += pow(3, Q, mod)
            ans %= mod
        elif s == 'C':
            a = pow(3, Q, mod)
            b = pow(3, i, mod)
            ans += a * b
            ans %= mod
            ans += pow(3, Q, mod)
            ans %= mod
            ans += pow(3, Q, mod)
            ans %= mod
    print(ans)
