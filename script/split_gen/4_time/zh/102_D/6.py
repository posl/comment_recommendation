def main():
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    ans=10**9
    t=0
    for i in range(n-1):
        t+=a[i]
        if t*2==s:
            ans=0
            break
        elif t*2>s:
            ans=min(ans,abs(t*2-s))
            ans=min(ans,abs(t*2-s+a[i+1]*2))
            break
        else:
            ans=min(ans,abs(t*2-s))
            ans=min(ans,abs(t*2-s+a[i+1]*2))
    print(ans)
