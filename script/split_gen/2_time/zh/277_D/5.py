def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    if n == 1:
        print(a[0])
        return
    
    b = []
    for i in range(n):
        b.append(a[i] % m)
    #print(b)
    
    c = []
    for i in range(n):
        c.append(a[i] // m)
    #print(c)
    
    d = []
    for i in range(n):
        d.append((m - b[i]) % m)
    #print(d)
    
    e = []
    for i in range(n):
        e.append((m - b[i] - 1) % m)
    #print(e)
    
    f = []
    for i in range(n):
        f.append((m - b[i] - 2) % m)
    #print(f)
    
    g = []
    for i in range(n):
        g.append((m - b[i] - 3) % m)
    #print(g)
    
    h = []
    for i in range(n):
        h.append((m - b[i] - 4) % m)
    #print(h)
    
    i = []
    for j in range(n):
        i.append((m - b[j] - 5) % m)
    #print(i)
    
    j = []
    for j in range(n):
        j.append((m - b[j] - 6) % m)
    #print(j)
    
    k = []
    for j in range(n):
        k.append((m - b[j] - 7) % m)
    #print(k)
    
    l = []
    for j in range(n):
        l.append((m - b[j] - 8) % m)
    #print(l)
    
    m = []
    for j in range(n):
        m.append((m - b[j] - 9) % m)
    #print(m)
    
    n = []
    for j in range(n):
        n.append((m - b[j] - 10) % m)
    #print(n)
    
    o = []
    for j in range(n):
        o.append((m - b[j] - 11) % m)
    #print(o)
    
    p = []
    for j
