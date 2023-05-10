def solve(n, a, b, c):
    a = [i-1 for i in a]
    b = [i-1 for i in b]
    c = [i-1 for i in c]
    b_count = {}
    for i in range(n):
        if b[i] in b_count:
            b_count[b[i]] += 1
        else:
            b_count[b[i]] = 1
    c_count = {}
    for i in range(n):
        if c[i] in c_count:
            c_count[c[i]] += 1
        else:
            c_count[c[i]] = 1
    ans = 0
    for i in range(n):
        if a[i] in b_count:
            ans += b_count[a[i]] * c_count[i]
    return ans
