def is_star(n,ab):
    a,b = [list(i) for i in zip(*ab)]
    a = [i-1 for i in a]
    b = [i-1 for i in b]
    c = [0]*n
    for i in a:
        c[i] += 1
    for i in b:
        c[i] += 1
    if max(c) == n-1 and min(c) == 1:
        return True
    else:
        return False
