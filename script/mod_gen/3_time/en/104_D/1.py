def main():
    s = input()
    mod = 10**9 + 7
    n = len(s)
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    q = s.count('?')
    abc = a*b*c
    ans = 0
    for i in range(n):
        if s[i] == '?':
            ans += abc*(pow(3, q-1, mod)) % mod
            ans %= mod
            q -= 1
        elif s[i] == 'A':
            ans += b*c*pow(3, q, mod) % mod
            ans %= mod
        elif s[i] == 'B':
            ans += a*c*pow(3, q, mod) % mod
            ans %= mod
        elif s[i] == 'C':
            ans += a*b*pow(3, q, mod) % mod
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()