def main():
    import sys
    input=sys.stdin.readline
    #functions
    def solve():
        for i in range(1,n):
            a[i]+=a[i-1]
        for i in range(1,n):
            b[i]=a[i-1]
        for i in range(1,n):
            c[i]=a[i-1]
        for i in range(1,n):
            d[i]=a[i-1]
        for i in range(1,n):
            if b[i-1]+p==b[i]:
                b[i]=b[i-1]
            else:
                b[i]=min(b[i-1],b[i])
        for i in range(1,n):
            if c[i-1]+q==c[i]:
                c[i]=c[i-1]
            else:
                c[i]=min(c[i-1],c[i])
        for i in range(1,n):
            if d[i-1]+r==d[i]:
                d[i]=d[i-1]
            else:
                d[i]=min(d[i-1],d[i])
        for i in range(1,n):
            if b[i-1]+p==b[i] and c[i-1]+q==c[i] and d[i-1]+r==d[i]:
                return "Yes"
        return "No"
    #inputs
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=[0]*n
    c=[0]*n
    d=[0]*n
    #solve
    print(solve())
