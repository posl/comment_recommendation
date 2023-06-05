def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.reverse()
    b=[0 for i in range(n)]
    b[0]=a[0]
    for i in range(1,n):
        if a[i]>b[i-1]:
            b[i]=a[i]
        else:
            b[i]=b[i-1]
    b.reverse()
    print(sum(b))
main()
