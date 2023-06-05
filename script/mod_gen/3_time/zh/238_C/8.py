def f(x):
    s = str(x)
    return len(s)
N = int(input())
mod = 998244353
ans = 0
for i in range(1, N+1):
    ans += i * f(i)
    ans %= mod
print(ans)

if __name__ == '__main__':
    f()