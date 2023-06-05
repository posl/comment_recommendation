def f(x):
    res = 0
    for i in range(n):
        res += x ^ a[i]
    return res
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(40, -1, -1):
    cnt0 = 0
    cnt1 = 0
    for j in range(n):
        if a[j] & (1 << i):
            cnt1 += 1
        else:
            cnt0 += 1
    if cnt0 >= cnt1:
        if ans + (1 << i) <= k:
            ans += 1 << i
print(f(ans))
