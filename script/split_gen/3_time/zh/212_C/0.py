def solve(n, m, a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 0x7fffffff
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans
