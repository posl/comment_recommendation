def solve():
    s = input()
    n = len(s)
    mod = 10**9+7
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    for i in range(n):
        if s[i] == "A":
            a[i+1] += 1
        elif s[i] == "B":
            b[i+1] += 1
        elif s[i] == "C":
            c[i+1] += 1
        else:
            a[i+1] += 1
            b[i+1] += 1
            c[i+1] += 1
    for i in range(n):
        a[i+1] += a[i]
        b[i+1] += b[i]
        c[i+1] += c[i]
    ans = 0
    for i in range(n):
        if s[i] == "B" or s[i] == "?":
            ans += a[i] * (c[n]-c[i+1])
            ans %= mod
    print(ans)
solve()
