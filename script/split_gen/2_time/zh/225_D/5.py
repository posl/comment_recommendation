def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
