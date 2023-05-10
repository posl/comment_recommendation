def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    left=-10**18
    right=10**18
    while left+1<right:
        x=(left+right)//2
        cnt=0
        for i in range(n):
            if a[i]<0:
                l,r=-1,n
                while l+1<r:
                    m=(l+r)//2
                    if a[m]*a[i]<x:
                        r=m
                    else:
                        l=m
                cnt+=n-r
            else:
                l,r=-1,n
                while l+1<r:
                    m=(l+r)//2
                    if a[m]*a[i]<x:
                        l=m
                    else:
                        r=m
                cnt+=r
            if a[i]**2<x:
                cnt-=1
        cnt//=2
        if cnt<k:
            left=x
        else:
            right=x
    print(left)
