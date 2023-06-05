def main():
    s = input()
    q = s.count('?')
    a = [0] * (q + 1)
    b = [0] * (q + 1)
    c = [0] * (q + 1)
    for i in range(q):
        a[i + 1] = a[i] * 3 + (s[i] == 'A')
        b[i + 1] = b[i] * 3 + (s[i] == 'B')
        c[i + 1] = c[i] * 3 + (s[i] == 'C')
    ans = 0
    for i in range(len(s)):
        if s[i] == 'B' or s[i] == '?':
            ans += a[q] * c[q] - a[q - 1] * c[q - 1]
            ans %= 1000000007
        if s[i] == 'A' or s[i] == '?':
            ans += b[q] * c[q] - b[q - 1] * c[q - 1]
            ans %= 1000000007
        if s[i] == '?':
            ans += b[q - 1] * c[q - 1] - a[q - 1] * c[q - 1]
            ans %= 1000000007
            ans += a[q - 1] * b[q - 1] - b[q - 1] * c[q - 1]
            ans %= 1000000007
            ans += a[q - 1] * c[q - 1] - a[q - 1] * b[q - 1]
            ans %= 1000000007
            q -= 1
    print(ans)

if __name__ == '__main__':
    main()