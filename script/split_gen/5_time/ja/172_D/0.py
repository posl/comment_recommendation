def f(x):
    ans = 0
    for i in range(1, x + 1):
        if x % i == 0:
            ans += 1
    return ans
N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += i * f(i)
print(ans)
