def f(x):
    if x == 1:
        return 1
    res = 2
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            res += i
            if x//i != i:
                res += x//i
    return res
N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i*f(i)
print(ans)
