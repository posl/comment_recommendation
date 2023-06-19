def solve(n,m):
    ans = 1
    for i in range(2,int(m**0.5)+1):
        cnt = 0
        while m%i == 0:
            cnt += 1
            m //= i
        ans *= comb(n+cnt-1,cnt)
        ans %= mod
    if m > 1:
        ans *= n
        ans %= mod
    return ans
mod = 10**9+7
n,m = map(int,input().split())
print(solve(n,m))
