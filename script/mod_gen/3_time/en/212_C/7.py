def binarySearch(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 10 ** 9 + 1
for i in range(n):
    j = binarySearch(b, a[i])
    if j < m:
        ans = min(ans, abs(a[i] - b[j]))
    if j > 0:
        ans = min(ans, abs(a[i] - b[j - 1]))
print(ans)

if __name__ == '__main__':
    binarySearch()