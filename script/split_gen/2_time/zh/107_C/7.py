def solve():
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    ans=float('inf')
    for i in range(n-k+1):
        left=x[i]
        right=x[i+k-1]
        if left*right<=0:
            ans=min(ans,min(-2*left+right,right-2*left))
        else:
            ans=min(ans,max(abs(left),abs(right)))
    print(ans)
