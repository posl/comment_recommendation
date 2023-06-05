def main():
    n,m=map(int,input().split())
    p=[0]*m
    y=[0]*m
    for i in range(m):
        p[i],y[i]=map(int,input().split())
    for i in range(m):
        p[i]=str(p[i])
        y[i]=str(y[i])
    for i in range(m):
        p[i]=p[i].zfill(6)
        y[i]=y[i].zfill(6)
    for i in range(m):
        p[i]=p[i]+y[i]
    p.sort()
    for i in range(m):
        p[i]=p[i][6:]
    for i in range(m):
        print(p[i])
