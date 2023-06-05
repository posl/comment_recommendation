def solve(n, k, a):
    ans = 0
    for i in range(k):
        ans += a[i]
    return ans - a[k - 1] // 2
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
