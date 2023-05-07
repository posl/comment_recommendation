def find(x, parents):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x], parents)
        return parents[x]
