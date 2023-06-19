def f(x):
    if x < 10:
        return x
    else:
        return f(x//10) + 1
N = int(input())
mod = 998244353
ans = 0
for i in range(1, N+1):
    ans += f(i)
    ans %= mod
print(ans)

if __name__ == '__main__':
    f()