def f(x):
    return len(str(x))
n = int(input())
ans = 0
mod = 998244353
for i in range(1, n+1):
    ans += i
    ans %= mod
    if i == n:
        break
    if f(i) == f(i+1):
        continue
    else:
        ans += i
        ans %= mod
print(ans)
