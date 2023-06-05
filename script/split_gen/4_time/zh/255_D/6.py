def solve(n, q, a, x):
    ans = []
    for i in range(q):
        y = x[i]
        s = 0
        for j in range(n):
            if a[j] > y:
                s += a[j] - y
            else:
                s += y - a[j]
        ans.append(s)
    return ans
