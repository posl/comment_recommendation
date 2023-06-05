def main():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    c = [0] * n
    q = [0] * n
    for i in range(n):
        if s[i] == 'A':
            a[i] = 1
        elif s[i] == 'B':
            b[i] = 1
        elif s[i] == 'C':
            c[i] = 1
        else:
            q[i] = 1
    for i in range(1, n):
        a[i] += a[i-1]
        b[i] += b[i-1]
        c[i] += c[i-1]
        q[i] += q[i-1]
    ans = 0
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            for j in range(i+1, n):
                if s[j] == 'C' or s[j] == '?':
                    ans += a[i] * (q[j] - q[i])
                    ans %= 10**9+7
    print(ans)
