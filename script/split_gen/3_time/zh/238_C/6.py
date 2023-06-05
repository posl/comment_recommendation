def f(x):
    if x < 10:
        return x
    else:
        return f(x//10) + 1
N = int(input())
mod = 998244353
ans = 0
for i in range(1, 19):
    if 10**i > N:
        break
    ans += (min(10**i-1, N) - 10**(i-1) + 1) * f(10**(i-1))
    ans %= mod
print(ans)
