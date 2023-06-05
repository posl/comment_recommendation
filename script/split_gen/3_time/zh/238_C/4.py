def f(x):
    return x
N = int(input())
ans = 0
for k in range(1, N+1):
    ans += f(k)
print(ans % 998244353)
