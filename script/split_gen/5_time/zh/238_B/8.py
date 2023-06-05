def solve(n, a):
    a = sorted(a)
    a = a[::-1]
    ans = 0
    for i in range(n):
        ans += a[i] * (-1)**i
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
