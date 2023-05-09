def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * (m + 1)
for i in range(n):
    for j in range(1, int(m ** 0.5) + 1):
        if a[i] % j == 0:
            l[j] = 1
            l[a[i] // j] = 1
l[1] = 1
for i in range(2, m + 1):
    if l[i] == 1:
        for j in range(i * 2, m + 1, i):
            l[j] = 0
ans = []
for i in range(1, m + 1):
    if l[i] == 1:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
