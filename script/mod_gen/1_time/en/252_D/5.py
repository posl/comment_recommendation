def solve(n, a):
    from collections import Counter
    c = Counter(a)
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) * (v - 2) // 6
    for i in range(n):
        ans -= c[a[i]] * (c[a[i]] - 1) // 2 * (c[a[i]] - 2) // 3
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
