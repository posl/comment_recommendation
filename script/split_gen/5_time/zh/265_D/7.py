def main():
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=[a[0]]
    for i in range(1,n):
        b.append(b[i-1]+a[i])
    c=[b[0]]
    for i in range(1,n):
        c.append(c[i-1]+b[i])
    d=[c[0]]
    for i in range(1,n):
        d.append(d[i-1]+c[i])
    e=[d[0]]
    for i in range(1,n):
        e.append(e[i-1]+d[i])
    f=[e[0]]
    for i in range(1,n):
        f.append(f[i-1]+e[i])
    g=[f[0]]
    for i in range(1,n):
        g.append(g[i-1]+f[i])
    h=[g[0]]
    for i in range(1,n):
        h.append(h[i-1]+g[i])
    i=[h[0]]
    for i in range(1,n):
        i.append(i[i-1]+h[i])
    j=[i[0]]
    for i in range(1,n):
        j.append(j[i-1]+i[i])
    k=[j[0]]
    for i in range(1,n):
        k.append(k[i-1]+j[i])
    l=[k[0]]
    for i in range(1,n):
        l.append(l[i-1]+k[i])
    m=[l[0]]
    for i in range(1,n):
        m.append(m[i-1]+l[i])
    n=[m[0]]
    for i in range(1,n):
        n.append(n[i-1]+m[i])
    o=[n[0]]
    for i in range(1,n):
        o.append(o[i-1]+n[i])
    p=[o[0]]
    for i in range(1,n):
        p.append(p[i-1]+o[i])
    q=[p[0]]
    for i in range(1,n):
        q.append(q[i-1]+p[i])
    r=[q[0]]
    for i in range(1,n):
        r.append(r[i-1]+q[i])
    s=[r[0]]
    for i in range(1,n):
        s
