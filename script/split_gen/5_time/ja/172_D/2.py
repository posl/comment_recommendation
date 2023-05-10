def f(x):
    if x == 1:
        return 1
    else:
        i = 2
        count = 2
        while i * i <= x:
            if i * i == x:
                count += 1
            elif x % i == 0:
                count += 2
            i += 1
        return count
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)
