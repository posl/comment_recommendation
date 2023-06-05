def f(x):
    if x < 10:
        return x
    else:
        return f(x // 10) + 1
n = int(input())
ans = 0
mod = 998244353
for i in range(1, n + 1):
    ans += f(i)
    ans %= mod
print(ans)

if __name__ == '__main__':
    f()