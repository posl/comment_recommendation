def main():
    s = input()
    c = 0
    h = 0
    o = 0
    k = 0
    u = 0
    d = 0
    a = 0
    i = 0
    for j in range(len(s)):
        if s[j] == 'c':
            c += 1
        elif s[j] == 'h':
            h += 1
        elif s[j] == 'o':
            o += 1
        elif s[j] == 'k':
            k += 1
        elif s[j] == 'u':
            u += 1
        elif s[j] == 'd':
            d += 1
        elif s[j] == 'a':
            a += 1
        elif s[j] == 'i':
            i += 1
    ans = 0
    ans += c * h * o * k * u * d * a * i
    ans %= 1000000007
    print(ans)
