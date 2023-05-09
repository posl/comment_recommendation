def main():
    s = input()
    mod = 10**9 + 7
    n = len(s)
    c = 0
    h = 0
    o = 0
    k = 0
    u = 0
    d = 0
    a = 0
    i = 0
    for j in range(n):
        if s[j] == 'c':
            c += 1
        elif s[j] == 'h':
            h += c
        elif s[j] == 'o':
            o += h
        elif s[j] == 'k':
            k += o
        elif s[j] == 'u':
            u += k
        elif s[j] == 'd':
            d += u
        elif s[j] == 'a':
            a += d
        elif s[j] == 'i':
            i += a
    print(i % mod)
main()

if __name__ == '__main__':
    main()