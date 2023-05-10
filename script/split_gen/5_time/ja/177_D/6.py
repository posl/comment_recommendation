def get_parent(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = get_parent(parents[x])
        return parents[x]
