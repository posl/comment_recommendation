def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],i+1])
    c = sorted(c,reverse=True)
    d = []
    for i in range(x):
        d.append(c[i][1])
    d = sorted(d)
    print(*d,sep="\n")
    c = c[x:]
    e = []
    for i in range(y):
        e.append(c[i][1])
    e = sorted(e)
    print(*e,sep="\n")
    c = c[y:]
    f = []
    for i in range(z):
        f.append(c[i][1])
    f = sorted(f)
    print(*f,sep="\n")
    c = c[z:]
    g = []
    for i in range(len(c)):
        g.append(c[i][1])
    g = sorted(g)
    print(*g,sep="\n")
