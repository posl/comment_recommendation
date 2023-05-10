def main():
    s = input()
    q = s.count('?')
    mod = 10**9 + 7
    a = 0
    b = 0
    c = 0
    for i in range(len(s)):
        if s[i] == 'A':
            a += pow(3, q, mod)
        elif s[i] == 'B':
            b += pow(3, q, mod)
        elif s[i] == 'C':
            c += pow(3, q, mod)
        else:
            a, b, c = (a*3 + pow(3, q-1, mod)) % mod, (b*3 + a) % mod, (c*3 + b) % mod
    print(c%mod)

if __name__ == '__main__':
    main()