def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = list(map(int, input().split()))
t = [0] * (m + 1)
for i in range(n):
    for j in range(1, int(m ** 0.5) + 1):
        if a[i] % j == 0:
            t[j] = 1
            t[a[i] // j] = 1
ans = []
for i in range(1, m + 1):
    if t[i] == 0:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
