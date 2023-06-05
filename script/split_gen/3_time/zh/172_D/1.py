def f(x):
    s = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            s += i
            if i != x / i:
                s += x / i
    return s
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)
