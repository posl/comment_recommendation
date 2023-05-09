def solve(s):
    from collections import defaultdict
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    for c in 'chokudai':
        if c not in d:
            return 0
    d = list(d.values())
    d.sort()
    a = d[0]
    d = d[1:]
    d = [i-a for i in d]
    d = [i%1000000007 for i in d]
    d = [i*(i+1)//2 for i in d]
    d = [i%1000000007 for i in d]
    d = [i*(i+1)//2 for i in d]
    d = [i%1000000007 for i in d]
    d = [i*(i+1)//2 for i in d]
    d = [i%1000000007 for i in d]
    d = [i*(i+1)//2 for i in d]
    d = [i%1000000007 for i in d]
    return d[0]
