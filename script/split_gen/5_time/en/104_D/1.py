def main():
    s = input()
    n = len(s)
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(n):
        a[i + 1] = a[i]
        b[i + 1] = b[i]
        c[i + 1] = c[i]
        if s[i] == "A":
            a[i + 1] += pow(3, s[:i].count("?"), 10 ** 9 + 7)
        elif s[i] == "B":
            b[i + 1] += pow(3, s[:i].count("?"), 10 ** 9 + 7)
        elif s[i] == "C":
            c[i + 1] += pow(3, s[:i].count("?"), 10 ** 9 + 7)
        else:
            a[i + 1] += 2 * pow(3, s[:i].count("?"), 10 ** 9 + 7)
            b[i + 1] += 2 * pow(3, s[:i].count("?"), 10 ** 9 + 7)
            c[i + 1] += 2 * pow(3, s[:i].count("?"), 10 ** 9 + 7)
    ans = 0
    for i in range(n):
        if s[i] == "B" or s[i] == "?":
            ans += a[i] * c[n] % (10 ** 9 + 7)
        if s[i] == "A" or s[i] == "?":
            ans += b[i] * c[n] % (10 ** 9 + 7)
        if s[i] == "?":
            ans += b[i] * c[n] % (10 ** 9 + 7)
            ans += a[i] * c[n] % (10 ** 9 + 7)
            ans += b[i] * a[n] % (10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)
