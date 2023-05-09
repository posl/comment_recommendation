def main():
    S = input()
    mod = 10**9 + 7
    a = S.count('A')
    b = S.count('B')
    c = S.count('C')
    q = S.count('?')
    ans = 0
    for i, s in enumerate(S):
        if s == 'A':
            ans += (b * pow(3, q, mod) + c * pow(3, q, mod)) * pow(3, q - i, mod)
        elif s == 'B':
            ans += (a * pow(3, q, mod) + c * pow(3, q, mod)) * pow(3, q - i, mod)
        elif s == 'C':
            ans += (a * pow(3, q, mod) + b * pow(3, q, mod)) * pow(3, q - i, mod)
        else:
            ans += (a * b * pow(3, q, mod) + a * c * pow(3, q, mod) + b * c * pow(3, q, mod)) * pow(3, q - i, mod)
        ans %= mod
    print(ans)
