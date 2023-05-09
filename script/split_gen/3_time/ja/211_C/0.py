def main():
    s = input()
    n = len(s)
    c = 0
    h = 0
    o = 0
    k = 0
    u = 0
    d = 0
    a = 0
    i = 0
    for si in s:
        if si == "c":
            c += 1
        elif si == "h":
            h += c
        elif si == "o":
            o += h
        elif si == "k":
            k += o
        elif si == "u":
            u += k
        elif si == "d":
            d += u
        elif si == "a":
            a += d
        elif si == "i":
            i += a
    print(i % (10**9 + 7))
