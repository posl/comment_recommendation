def main():
    s = input()
    mod = 10**9 + 7
    c = 0
    h = 0
    o = 0
    k = 0
    u = 0
    d = 0
    a = 0
    i = 0
    for x in s:
        if x == 'c':
            c += 1
        elif x == 'h':
            h += c
        elif x == 'o':
            o += h
        elif x == 'k':
            k += o
        elif x == 'u':
            u += k
        elif x == 'd':
            d += u
        elif x == 'a':
            a += d
        elif x == 'i':
            i += a
    print(i % mod)

if __name__ == '__main__':
    main()