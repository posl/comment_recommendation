def main():
    s = input()
    n = len(s)
    a = [0]*n
    b = [0]*n
    c = [0]*n
    q = [0]*n
    for i in range(n):
        if s[i] == 'A':
            a[i] += 1
        elif s[i] == 'B':
            b[i] += 1
        elif s[i] == 'C':
            c[i] += 1
        elif s[i] == '?':
            q[i] += 1
        if i > 0:
            a[i] += a[i-1]
            b[i] += b[i-1]
            c[i] += c[i-1]
            q[i] += q[i-1]
    ans = 0
    mod = 10**9+7
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            ans += a[i]*(pow(3, q[i], mod))%mod
            ans %= mod
            ans += c[i]*(pow(3, q[i], mod))%mod
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()