def count_underline(s):
    n = len(s)
    c = s.count("c")
    h = s.count("h")
    o = s.count("o")
    k = s.count("k")
    u = s.count("u")
    d = s.count("d")
    a = s.count("a")
    i = s.count("i")
    mod = 10**9+7
    if n < 8 or c < 1 or h < 1 or o < 1 or k < 1 or u < 1 or d < 1 or a < 1 or i < 1:
        return 0
    else:
        return (c*h*o*k*u*d*a*i) % mod

if __name__ == '__main__':
    count_underline()