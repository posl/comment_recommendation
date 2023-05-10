def f(x):
    if x == 1:
        return 1
    else:
        count = 0
        for i in range(1, int(x**0.5)+1):
            if x % i == 0:
                count += 2
        if int(x**0.5) == x**0.5:
            count -= 1
        return count
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)
