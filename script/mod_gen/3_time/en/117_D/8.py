def solve(n, k, a): # n: number of integers, k: max integer, a: list of integers
    a = sorted(a)
    b = [a[0]]
    for i in range(1, n):
        b.append(a[i] ^ a[i-1])
    b.append(k ^ a[-1])
    b = sorted(b)
    c = [b[0]]
    for i in range(1, n+1):
        c.append(b[i] ^ b[i-1])
    c = sorted(c)
    d = [c[0]]
    for i in range(1, n+2):
        d.append(c[i] ^ c[i-1])
    d = sorted(d)
    e = [d[0]]
    for i in range(1, n+3):
        e.append(d[i] ^ d[i-1])
    e = sorted(e)
    f = [e[0]]
    for i in range(1, n+4):
        f.append(e[i] ^ e[i-1])
    f = sorted(f)
    g = [f[0]]
    for i in range(1, n+5):
        g.append(f[i] ^ f[i-1])
    g = sorted(g)
    h = [g[0]]
    for i in range(1, n+6):
        h.append(g[i] ^ g[i-1])
    h = sorted(h)
    i = [h[0]]
    for i in range(1, n+7):
        i.append(h[i] ^ h[i-1])
    i = sorted(i)
    j = [i[0]]
    for i in range(1, n+8):
        j.append(i[i] ^ i[i-1])
    j = sorted(j)
    k = [j[0]]
    for i in range(1, n+9):
        k.append(j[i] ^ j[i-1])
    k = sorted(k)
    l = [k[0]]
    for i in range(1, n+10):
        l.append(k[i] ^ k[i-1])
    l = sorted(l)
    m = [l[0]]
    for i in range(1, n+11):
        m.append(l[i] ^ l[i-1])
    m = sorted(m)
    n = [m[

if __name__ == '__main__':
    solve()