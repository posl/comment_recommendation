def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]
