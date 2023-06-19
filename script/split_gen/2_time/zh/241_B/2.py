def solve(n, m, a, b):
    a.sort()
    b.sort()
    if n < m:
        return "No"
    else:
        for i in range(m):
            if a[i] >= b[i]:
                return "No"
        return "Yes"
