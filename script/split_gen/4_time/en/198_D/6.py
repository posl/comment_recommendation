def solve(s1, s2, s3):
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    d = {}
    for s in s1 + s2 + s3:
        d[s] = -1
    if len(d) > 10:
        return 'UNSOLVABLE'
    for i in range(10):
        if i in d.values():
            continue
        d[s1[0]] = i
        for j in range(10):
            if j in d.values():
                continue
            d[s2[0]] = j
            for k in range(10):
                if k in d.values():
                    continue
                d[s3[0]] = k
                if d[s1[0]] + d[s2[0]] == d[s3[0]]:
                    if len(s1) == 1 and len(s2) == 1 and len(s3) == 1:
                        return '%d\n%d\n%d' % (d[s1[0]], d[s2[0]], d[s3[0]])
                    elif len(s1) == 1 or len(s2) == 1 or len(s3) == 1:
                        continue
                    else:
                        n1 = 0
                        n2 = 0
                        n3 = 0
                        for s in s1:
                            n1 = n1 * 10 + d[s]
                        for s in s2:
                            n2 = n2 * 10 + d[s]
                        for s in s3:
                            n3 = n3 * 10 + d[s]
                        if n1 + n2 == n3:
                            return '%d\n%d\n%d' % (n1, n2, n3)
                d[s3[0]] = -1
            d[s2[0]] = -1
        d[s1[0]] = -1
    return 'UNSOLVABLE'
s1 = input()
s2 = input()
s3 = input()
print(solve(s1, s2, s3))
