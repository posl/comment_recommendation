def solve(n,k):
    ans = 0
    for a in range(1,n+1):
        ans += (n//a)*((k+a)//k)
        if (n%a) >= (k-1):
            ans += (n%a)-(k-1)
    return ans
n,k = map(int,input().split())
print(solve(n,k))
