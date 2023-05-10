def f(x):
    ret = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ret += 1
            if i != x // i:
                ret += 1
    return ret
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)
