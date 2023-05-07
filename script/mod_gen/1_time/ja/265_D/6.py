def solve():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                ans = max(ans,a[i]*p+a[j]*q+a[k]*r)
    print(ans)

if __name__ == '__main__':
    solve()