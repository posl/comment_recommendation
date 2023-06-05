def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    c=[]
    for i in range(m):
        bi,ci=map(int,input().split())
        b.append(bi)
        c.append(ci)
    b.sort()
    c.sort()
    sum=0
    for i in range(m):
        if(a[n-1]>c[m-i-1]):
            sum+=a[n-1]
            n-=1
        else:
            sum+=c[m-i-1]
            if(b[m-i-1]>n):
                n=0
            else:
                n-=b[m-i-1]
    for i in range(n):
        sum+=a[i]
    print(sum)
