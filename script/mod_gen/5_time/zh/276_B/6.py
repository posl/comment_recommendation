def main():
    n,m=map(int,input().split())
    a,b=[],[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(1,n+1):
        count=0
        for j in range(m):
            if i==a[j] or i==b[j]:
                count+=1
        print(count,end=" ")
        for j in range(m):
            if i==a[j] or i==b[j]:
                if i==a[j]:
                    print(b[j],end=" ")
                else:
                    print(a[j],end=" ")
        print()
main()
