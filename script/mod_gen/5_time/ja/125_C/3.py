def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
left = [0] * n
right = [0] * n
left[0] = a[0]
right[-1] = a[-1]
for i in range(1, n):
    left[i] = gcd(left[i - 1], a[i])
for i in range(n - 2, -1, -1):
    right[i] = gcd(right[i + 1], a[i])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, right[i + 1])
    elif i == n - 1:
        ans = max(ans, left[i - 1])
    else:
        ans = max(ans, gcd(left[i - 1], right[i + 1]))
print(ans)

if __name__ == '__main__':
    gcd()