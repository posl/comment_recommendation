def check(n, m, a, b, c, d):
    if m == 0:
        return True
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if i in a and j in a:
                if not (a.index(i) == a.index(j) and b.index(i) == b.index(j)):
                    continue
            if i in c and j in c:
                if not (c.index(i) == c.index(j) and d.index(i) == d.index(j)):
                    continue
            if i in a and j in c:
                if not (a.index(i) == c.index(j) and b.index(i) == d.index(j)):
                    continue
            if i in c and j in a:
                if not (c.index(i) == a.index(j) and d.index(i) == b.index(j)):
                    continue
            if i in a and j in b:
                if not (a.index(i) == b.index(j) and b.index(i) == a.index(j)):
                    continue
            if i in c and j in d:
                if not (c.index(i) == d.index(j) and d.index(i) == c.index(j)):
                    continue
            if i in b and j in a:
                if not (b.index(i) == a.index(j) and a.index(i) == b.index(j)):
                    continue
            if i in d and j in c:
                if not (d.index(i) == c.index(j) and c.index(i) == d.index(j)):
                    continue
            if i in b and j in b:
                if not (b.index(i) == b.index(j) and a.index(i) == a.index(j)):
                    continue
            if i in d and j in d:
                if not (d.index(i) == d.index(j) and c.index(i) == c.index(j)):
                    continue
            if i in b and j in d:
                if not (b.index(i) == d.index(j) and a.index(i) == c.index(j)):
                    continue
            if i in d and j in b:
                if not (

if __name__ == '__main__':
    check()