def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
max_a = max(a)
gcd_a = [0] * (max_a + 1)
for i in range(n):
    for j in range(1, int(max_a ** 0.5) + 1):
        if a[i] % j == 0:
            gcd_a[j] = 1
            gcd_a[a[i] // j] = 1
ans = []
for i in range(1, m + 1):
    if gcd_a[i] == 0:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
