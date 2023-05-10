def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],b[i],i+1])
    c.sort(reverse=True)
    d = []
    for i in range(x):
        d.append([c[i][1]+c[i][2],c[i][1],c[i][2],c[i][3]])
    d.sort(reverse=True)
    e = []
    for i in range(y):
        e.append([c[i+x][2],c[i+x][1],c[i+x][2],c[i+x][3]])
    e.sort(reverse=True)
    f = []
    for i in range(z):
        f.append([c[i+x+y][0],c[i+x+y][1],c[i+x+y][2],c[i+x+y][3]])
    f.sort(reverse=True)
    g = []
    for i in range(x+y+z):
        g.append([c[i][3]])
    for i in range(x):
        g[d[i][0]-1].append(d[i][3])
    for i in range(y):
        g[e[i][0]-1].append(e[i][3])
    for i in range(z):
        g[f[i][0]-1].append(f[i][3])
    g.sort()
    for i in range(n):
        if len(g[i]) > 1:
            for j in range(len(g[i])-1):
                print(g[i][j+1])
        else:
            print(g[i][0])
