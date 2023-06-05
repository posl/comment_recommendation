def main():
    s = input()
    n = len(s)
    q = s.count('?')
    mod = 10**9 + 7
    ans = 0
    for i in range(n-2):
        if s[i] == 'A' or s[i] == '?':
            a = 3**q % mod
            b = 3**(q-1) % mod
            c = 3**(q-1) % mod
            ans += a+b+c
            ans %= mod
        if s[i] == 'B' or s[i] == '?':
            a = 3**q % mod
            b = 3**(q-1) % mod
            c = 3**(q-1) % mod
            ans += a+b+c
            ans %= mod
        if s[i] == 'C' or s[i] == '?':
            a = 3**q % mod
            b = 3**(q-1) % mod
            c = 3**(q-1) % mod
            ans += a+b+c
            ans %= mod
        if s[i] == '?':
            q -= 1
    print(ans)

if __name__ == '__main__':
    main()