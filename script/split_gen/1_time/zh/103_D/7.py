def find_root(x, parents):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_root(parents[x], parents)
        return parents[x]
