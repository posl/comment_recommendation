def f(x):
    if x == 1:
        return 1
    else:
        cnt = 0
        for i in range(1, int(x**0.5)+1):
            if x % i == 0:
                cnt += 2
        if int(x**0.5)**2 == x:
            cnt -= 1
        return cnt
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)
