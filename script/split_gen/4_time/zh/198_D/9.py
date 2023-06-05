def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set()
    for c in s1:
        s.add(c)
    for c in s2:
        s.add(c)
    for c in s3:
        s.add(c)
    if len(s) > 10:
        print('UNSOLVABLE')
        return
    s = list(s)
    n = len(s)
    for i in range(10 ** n):
        a = str(i).zfill(n)
        if len(set(a)) < n:
            continue
        m = {}
        for j in range(n):
            m[s[j]] = a[j]
        if m[s1[0]] == '0' or m[s2[0]] == '0' or m[s3[0]] == '0':
            continue
        n1 = 0
        n2 = 0
        n3 = 0
        for c in s1:
            n1 = n1 * 10 + int(m[c])
        for c in s2:
            n2 = n2 * 10 + int(m[c])
        for c in s3:
            n3 = n3 * 10 + int(m[c])
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')
