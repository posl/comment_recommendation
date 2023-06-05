def f(a,b,n):
    MOD = 10**9 + 7
    ans = pow(n,2,MOD)
    ans -= n
    ans -= n
    ans += 1
    ans %= MOD
    ans -= n-a+1
    ans %= MOD
    ans -= n-b+1
    ans %= MOD
    ans += n-a-b+2
    ans %= MOD
    return ans
n,a,b = map(int,input().split())
print(f(a,b,n))
