def main():
    s = input()
    n = len(s)
    q = s.count('?')
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            a = 0
            c = 0
            for j in range(i, n):
                if s[j] == 'A':
                    a += 1
                elif s[j] == 'C':
                    c += 1
                elif s[j] == '?':
                    ans += pow(3, q - 1, mod) * (pow(3, a, mod) + pow(3, c, mod)) % mod
                    ans %= mod
                    q -= 1
                    a += 1
                    c += 1
    print(ans)
main()
