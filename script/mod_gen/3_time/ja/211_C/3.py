def main():
    S = input()
    mod = 10**9 + 7
    ans = 1
    c = 0
    h = 0
    o = 0
    k = 0
    u = 0
    d = 0
    a = 0
    i = 0
    for s in S:
        if s == "c":
            c += 1
        elif s == "h":
            h += c
        elif s == "o":
            o += h
        elif s == "k":
            k += o
        elif s == "u":
            u += k
        elif s == "d":
            d += u
        elif s == "a":
            a += d
        elif s == "i":
            i += a
    print(i % mod)

if __name__ == '__main__':
    main()