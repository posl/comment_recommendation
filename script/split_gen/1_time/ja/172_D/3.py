def f(x):
    i = 1
    count = 0
    while i*i <= x:
        if x % i == 0:
            count += 2
        if i*i == x:
            count -= 1
        i += 1
    return count
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i*f(i)
print(ans)
