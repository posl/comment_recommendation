def main():
    n, m, q = map(int, input().split())
    a = [0] * q
    b = [0] * q
    c = [0] * q
    d = [0] * q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    ans = 0
    for A in range(1 << n):
        ok = True
        for i in range(q):
            if ((A >> a[i]) & 1) ^ ((A >> b[i]) & 1) != c[i]:
                ok = False
        if ok:
            now = 0
            for i in range(n):
                if (A >> i) & 1:
                    now += i + 1
            ans = max(ans, now)
    print(ans)
