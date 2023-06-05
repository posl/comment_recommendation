def count_pairs(n, a):
    d = {}
    for i in range(n):
        r = a[i] % 200
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    count = 0
    for k in d:
        if d[k] > 1:
            count += (d[k] - 1) * d[k] // 2
    return count
