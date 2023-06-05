def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1 + s2 + s3)
    if len(s) > 10:
        print("UNSOLVABLE")
        return
    s = list(s)
    n = len(s)
    if n > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** n):
        t = str(i).zfill(n)
        if len(set(t)) != n:
            continue
        d = {}
        for j in range(n):
            d[s[j]] = t[j]
        if d[s1[0]] == '0' or d[s2[0]] == '0' or d[s3[0]] == '0':
            continue
        n1 = int("".join([d[c] for c in s1]))
        n2 = int("".join([d[c] for c in s2]))
        n3 = int("".join([d[c] for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
solve()
