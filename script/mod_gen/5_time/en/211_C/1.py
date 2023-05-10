def main():
    S = input()
    c = 0
    h = 0
    o = 0
    k = 0
    u = 0
    d = 0
    a = 0
    i = 0
    for s in S:
        if s == 'c':
            c += 1
        elif s == 'h':
            h += 1
        elif s == 'o':
            o += 1
        elif s == 'k':
            k += 1
        elif s == 'u':
            u += 1
        elif s == 'd':
            d += 1
        elif s == 'a':
            a += 1
        elif s == 'i':
            i += 1
    print(c*h*o*k*u*d*a*i)

if __name__ == '__main__':
    main()