def main():
    s = input()
    q = s.count('?')
    mod = 10**9 + 7
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
    for i in range(len(s)):
        if s[i] == 'A':
            a -= 1
        elif s[i] == 'B':
            b -= 1
        elif s[i] == 'C':
            c -= 1
        elif s[i] == '?':
            ans += (a * pow(3, q, mod) + b * pow(3, q-1, mod) + c * pow(3, q-1, mod)) % mod
            q -= 1
    print(ans % mod)
