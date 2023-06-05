def f(x):
    ret = 0
    for i in range(1, x+1):
        if x % i == 0:
            ret += 1
    return ret
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)
