def f(n):
    if n == 0:
        return 0
    return 2 * f(n // 2) + (n % 2)
k = int(input())
left = 0
right = 10 ** 18
while right - left > 1:
    mid = (left + right) // 2
    if f(mid) < k:
        left = mid
    else:
        right = mid
ans = ""
for i in range(left + 1, right + 1):
    if f(i) == k:
        ans = str(i)
        break
print(ans)
