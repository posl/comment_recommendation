def sol():
    import sys
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(1,n+1):
        if i==a[a[i-1]-1]:
            ans+=1
    print(ans//2)
sol()
