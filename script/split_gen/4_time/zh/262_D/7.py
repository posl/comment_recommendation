def func(a):
    return sum(a) % len(a) == 0
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2**n - 1):
    b = []
    for j in range(n):
        if i >> j & 1:
            b.append(a[j])
    if func(b):
        ans += 1
print(ans)
