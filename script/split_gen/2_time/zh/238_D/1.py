def f(x):
    return x
N = int(input())
mod = 998244353
ans = 0
for i in range(1, N+1):
    ans += f(i)
    ans %= mod
print(ans)
