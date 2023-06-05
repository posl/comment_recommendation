def f(x):
    res = 0
    for i in range(1, x+1):
        if x % i == 0:
            res += 1
    return res
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)
