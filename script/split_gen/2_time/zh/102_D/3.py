def solve(n, a):
    a = [0] + a + [0]
    for i in range(n):
        a[i + 1] += a[i]
    ans = 10 ** 9
    l = 0
    r = 3
    for i in range(1, n - 2):
        while l < i - 1 and abs(a[l] - a[i] - a[i]) >= abs(a[l + 1] - a[i] - a[i]):
            l += 1
        while r < n - 1 and abs(a[r] - a[n] - a[n] + a[i]) >= abs(a[r + 1] - a[n] - a[n] + a[i]):
            r += 1
        ans = min(ans, max(abs(a[l] - a[i] - a[i]), abs(a[r] - a[n] - a[n] + a[i])))
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
