def solve(n, k):
    ans = 0
    for i in range(1, n + 1):
        p = 1
        while i < k:
            i *= 2
            p /= 2
        ans += p
    return ans / n
n, k = map(int, input().split())
print(solve(n, k))
