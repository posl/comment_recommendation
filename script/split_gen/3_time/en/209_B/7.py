def check(x,n,a):
    for i in range(n):
        if i%2==0:
            x-=a[i]
        else:
            x-=a[i]-1
        if x<0:
            return False
    return True
n,x=map(int,input().split())
a=list(map(int,input().split()))
