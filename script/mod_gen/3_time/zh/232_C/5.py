def main():
    n,m=map(int,input().split())
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(m):
        a1,b1=map(int,input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1,d1=map(int,input().split())
        c.append(c1)
        d.append(d1)
    for i in range(m):
        if a[i]>c[i]:
            a[i],c[i]=c[i],a[i]
            b[i],d[i]=d[i],b[i]
    for i in range(m):
        for j in range(m):
            if a[i]==c[j] and b[i]==d[j]:
                c[i],c[j]=c[j],c[i]
                d[i],d[j]=d[j],d[i]
    count=0
    for i in range(m):
        if a[i]==c[i] and b[i]==d[i]:
            count+=1
    if count==m:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()