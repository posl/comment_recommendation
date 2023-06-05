def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]
