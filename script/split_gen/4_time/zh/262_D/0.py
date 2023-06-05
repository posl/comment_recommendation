def f(n):
    if n == 1:
        return 1
    return f(n-1) + 2**(n-1)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for j in range(n-i+1):
        if sum(a[j:j+i]) % i == 0:
            ans += 1
print(ans)
