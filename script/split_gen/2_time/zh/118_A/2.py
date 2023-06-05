def xor_sum(a, b):
    if a == b:
        return a
    if b - a == 1:
        return a ^ b
    if a % 2 == 0 and b % 2 == 0:
        return xor_sum(a // 2, b // 2) * 2
    if a % 2 == 0 and b % 2 == 1:
        return xor_sum(a // 2, b // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 0:
        return xor_sum((a + 1) // 2, b // 2) * 2
    if a % 2 == 1 and b % 2 == 1:
        return xor_sum((a + 1) // 2, b // 2) * 2 + 1
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(41, -1, -1):
    count = 0
    for j in range(n):
        if a[j] >> i & 1:
            count += 1
    if count <= n // 2:
        continue
    if ans + (1 << i) <= k:
        ans += 1 << i
s = 0
for i in range(n):
    s += ans ^ a[i]
print(s)
