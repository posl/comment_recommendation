def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for i in range(q)]
    a.sort()
    b = [a[i]-a[i-1] for i in range(1,n)]
    b.sort()
    c = [b[i]-b[i-1] for i in range(1,n-1)]
    c.sort()
    d = [c[i]-c[i-1] for i in range(1,n-2)]
    d.sort()
    e = [d[i]-d[i-1] for i in range(1,n-3)]
    e.sort()
    f = [e[i]-e[i-1] for i in range(1,n-4)]
    f.sort()
    g = [f[i]-f[i-1] for i in range(1,n-5)]
    g.sort()
    h = [g[i]-g[i-1] for i in range(1,n-6)]
    h.sort()
    i = [h[i]-h[i-1] for i in range(1,n-7)]
    i.sort()
    j = [i[i]-i[i-1] for i in range(1,n-8)]
    j.sort()
    k = [j[i]-j[i-1] for i in range(1,n-9)]
    k.sort()
    l = [k[i]-k[i-1] for i in range(1,n-10)]
    l.sort()
    m = [l[i]-l[i-1] for i in range(1,n-11)]
    m.sort()
    n = [m[i]-m[i-1] for i in range(1,n-12)]
    n.sort()
    o = [n[i]-n[i-1] for i in range(1,n-13)]
    o.sort()
    p = [o[i]-o[i-1] for i in range(1,n-14)]
    p.sort()
    q = [p[i]-p[i-1] for i in range(1,n-15)]
    q.sort()
    r = [q[i]-q[i-1] for i in range(1,n-16)]
    r.sort()
    s = [r[i]-r[i-1] for i in range(1,n-17
