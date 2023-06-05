def solve(n, a):
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    return ans
n = int(input())
a = [int(i) for i in input().split()]
print(solve(n, a))
