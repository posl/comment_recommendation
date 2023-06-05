def binary_search(a, b, x):
    left = 0
    right = len(a) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if x < a[mid]:
            right = mid
        else:
            left = mid
    return abs(x - a[left]) if abs(x - a[left]) < abs(x - a[right]) else abs(x - a[right])
a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]
for i in range(q):
    ans = 10**20
    ans = min(ans, binary_search(s, t, x[i]))
    ans = min(ans, binary_search(t, s, x[i]))
    print(ans)
