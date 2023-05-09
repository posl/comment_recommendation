def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a
n = int(input())
a = list(map(int, input().split()))
max_gcd = 0
for i in range(2, 1001):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if count > max_gcd:
        max_gcd = count
        ans = i
print(ans)
