def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
n = int(input())
a = list(map(int, input().split()))
gcd_a = [a[0]]
for i in range(1,n):
    gcd_a.append(gcd(gcd_a[i-1], a[i]))
ans = 0
for i in range(n-1):
    if gcd_a[i] == a[i]:
        ans += 1
print(ans+n)
