def solve(n, a):
    from collections import Counter
    c = Counter(a)
    v = c.values()
    ans = 0
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            for k in range(j+1, len(v)):
                ans += v[i] * v[j] * v[k]
    return ans
