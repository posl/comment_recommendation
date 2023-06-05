def solve(n,k):
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += n*i-i*(i-1)//2+1
        ans %= mod
    return ans
n,k = map(int,input().split())
print(solve(n,k))
