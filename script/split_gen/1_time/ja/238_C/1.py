def f(x):
    if x < 10:
        return x
    else:
        return 9 + f(x // 10)
N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += f(i)
print(ans % 998244353)
