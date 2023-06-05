def f(x):
    res = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res += i
            if i != x // i:
                res += x // i
    return res
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)
