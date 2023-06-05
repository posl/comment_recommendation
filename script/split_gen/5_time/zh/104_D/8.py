def main():
    s = input()
    q = s.count("?")
    a = [0] * (q + 1)
    b = [0] * (q + 1)
    c = [0] * (q + 1)
    a[0] = 1
    b[0] = 1
    c[0] = 1
    for i in range(len(s)):
        if s[i] == "A":
            a[1] += a[0]
        elif s[i] == "B":
            b[1] += b[0]
        elif s[i] == "C":
            c[1] += c[0]
        else:
            a[1] += a[0]
            b[1] += b[0]
            c[1] += c[0]
        a[0] = a[1]
        b[0] = b[1]
        c[0] = c[1]
        a[1] %= 1000000007
        b[1] %= 1000000007
        c[1] %= 1000000007
    print(c[0])
