def f(x):
    if x < 10:
        return x
    else:
        return 1 + f(x//10)
n = int(input())
mod = 998244353
ans = 0
for i in range(1, n+1):
    ans += f(i)
    ans %= mod
print(ans)

if __name__ == '__main__':
    f()