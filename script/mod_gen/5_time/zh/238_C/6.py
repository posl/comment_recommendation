def f(x):
    return x if x < 10 else 1 + f(x // 10)
N = int(input())
MOD = 998244353
ans = 0
for i in range(1, 19):
    l = 10 ** (i - 1)
    r = min(N, 10 ** i - 1)
    if l <= N:
        ans += (r + l) * (r - l + 1) // 2 * i
        ans %= MOD
print(ans)

if __name__ == '__main__':
    f()