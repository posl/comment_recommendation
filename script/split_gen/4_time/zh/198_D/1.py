def solve(s1, s2, s3):
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    d = {}
    for c in s1 + s2 + s3:
        d[c] = 0
    if len(d) > 10:
        return "UNSOLVABLE"
    d = list(d.keys())
    for i in range(10 ** len(d)):
        x = str(i).zfill(len(d))
        for j in range(len(d)):
            d[j] = x[j]
        if check(s1, s2, s3, d):
            return "\n".join([s1, s2, s3])
    return "UNSOLVABLE"
