def f(x):
    i = 1
    cnt = 0
    while i*i <= x:
        if x%i == 0:
            cnt += 1
            if i*i != x:
                cnt += 1
        i += 1
    return cnt
n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i*f(i)
print(ans)
