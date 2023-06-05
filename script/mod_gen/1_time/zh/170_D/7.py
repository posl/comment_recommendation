def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
left = [0] * n
right = [0] * n
left[0] = a[0]
right[n - 1] = a[n - 1]
for i in range(1, n):
    left[i] = gcd(left[i - 1], a[i])
for i in range(n - 2, -1, -1):
    right[i] = gcd(right[i + 1], a[i])
ans = 1
for i in range(n):
    if i == 0:
        tmp = right[1]
    elif i == n - 1:
        tmp = left[n - 2]
    else:
        tmp = gcd(left[i - 1], right[i + 1])
    ans = max(ans, tmp)
print(ans)

if __name__ == '__main__':
    gcd()