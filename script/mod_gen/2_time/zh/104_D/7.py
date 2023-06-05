def solve():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(n):
        a[i + 1] = a[i] + (s[i] == 'A')
        b[i + 1] = b[i] + (s[i] == 'B')
        c[i + 1] = c[i] + (s[i] == 'C')
    ans = 0
    q = 0
    for i in range(n):
        if s[i] == 'A':
            ans += b[n] - b[i + 1]
            ans += c[n] - c[i + 1]
            ans += q
        elif s[i] == 'B':
            ans += a[n] - a[i + 1]
            ans += c[n] - c[i + 1]
            q += 1
        elif s[i] == 'C':
            ans += a[n] - a[i + 1]
            ans += b[n] - b[i + 1]
    for i in range(n):
        if s[i] == '?':
            ans = (ans * 3 + q) % mod
            q = q * 3 % mod
    print(ans % mod)

if __name__ == '__main__':
    solve()