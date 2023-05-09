def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
left = [0] * n
right = [0] * n
left[0] = a[0]
right[n-1] = a[n-1]
for i in range(1, n):
    left[i] = gcd(left[i-1], a[i])
    right[n-i-1] = gcd(right[n-i], a[n-i-1])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, right[1])
    elif i == n-1:
        ans = max(ans, left[n-2])
    else:
        ans = max(ans, gcd(left[i-1], right[i+1]))
print(ans)
