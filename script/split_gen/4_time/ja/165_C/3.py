def score(a):
    ans = 0
    for i in range(Q):
        if a[b[i]-1] - a[a[i]-1] == c[i]:
            ans += d[i]
    return ans
