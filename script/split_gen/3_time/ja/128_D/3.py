def main():
    n,k=map(int,input().split())
    v=list(map(int,input().split()))
    ans=0
    for i in range(min(n,k)+1):
        for j in range(min(n,k)-i+1):
            w=v[:i]+v[n-j:]
            w.sort()
            for l in range(min(len(w),k-i-j)):
                if w[l]<0:
                    w[l]=0
            ans=max(ans,sum(w))
    print(ans)
