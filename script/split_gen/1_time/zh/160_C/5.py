def solve(k, n, a):
    a.sort()
    a.append(a[0] + k)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i + 1] - a[i])
    return k - ans
k, n = map(int, input().split())
a = list(map(int, input().split()))
print(solve(k, n, a))
