def solve(n, a):
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
