def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    a.append(n+1)
    s = []
    for i in range(m+1):
        if a[i+1] - a[i] > 1:
            s.append(a[i+1] - a[i] - 1)
    if len(s) == 0:
        return 0
    k = min(s)
    ans = 0
    for i in range(len(s)):
        ans += (s[i] + k - 1) // k
    return ans
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
