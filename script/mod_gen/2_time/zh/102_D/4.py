def solve():
    n = int(input())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    ans = 10**9
    for i in range(1,n-2):
        l = 0
        r = i
        while l+1<r:
            m = (l+r)//2
            if s[m]<=s[i+1]-s[m]:
                l = m
            else:
                r = m
        p = s[l]
        q = s[i+1]-s[l]
        l = i+1
        r = n
        while l+1<r:
            m = (l+r)//2
            if s[m]-s[i+1]<=s[n]-s[m]:
                l = m
            else:
                r = m
        r = l
        l = i+1
        while l+1<r:
            m = (l+r)//2
            if s[m]-s[i+1]<=s[n]-s[m]:
                l = m
            else:
                r = m
        r = l
        s = s[n]-s[r]
        r = s[i+1]-s[l]
        ans = min(ans,max(p,q,r,s)-min(p,q,r,s))
        ans = min(ans,max(p,q,s-r,s)-min(p,q,s-r,s))
        ans = min(ans,max(p,r,s-q,s)-min(p,r,s-q,s))
        ans = min(ans,max(q,r,s-p,s)-min(q,r,s-p,s))
        ans = min(ans,max(p,s-q-r,s)-min(p,s-q-r,s))
        ans = min(ans,max(q,s-p-r,s)-min(q,s-p-r,s))
        ans = min(ans,max(r,s-p-q,s)-min(r,s-p-q,s))
    print(ans)

if __name__ == '__main__':
    solve()