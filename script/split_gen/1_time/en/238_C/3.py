def f(x):
    n = len(str(x))
    return (x-10**(n-1)+1)*n
N = int(input())
ans = 0
for i in range(1,10):
    ans += f(min(10**i-1,N))
    if 10**i > N:
        break
print(ans%(998244353))
