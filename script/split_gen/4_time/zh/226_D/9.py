def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
xy.sort()
d={}
for i in range(n):
    for j in range(i+1,n):
        x=xy[j][0]-xy[i][0]
        y=xy[j][1]-xy[i][1]
        g=gcd(x,y)
        if g==0:
            g=1
        x//=g
        y//=g
        if x<0:
            x,y=-x,-y
        elif x==0 and y<0:
            y=-y
        if (x,y) in d:
            d[(x,y)]+=1
        else:
            d[(x,y)]=1
print(n-max(d.values()))
