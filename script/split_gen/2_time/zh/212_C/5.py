def read_ints():
    return [int(x) for x in input().split()]
n,m = read_ints()
a = read_ints()
b = read_ints()
a.sort()
b.sort()
ans = 10**9
j = 0
for i in range(n):
    while j < m and b[j] <= a[i]:
        ans = min(ans, a[i] - b[j])
        j += 1
    if j < m:
        ans = min(ans, b[j] - a[i])
print(ans)
