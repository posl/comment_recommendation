def f(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)
