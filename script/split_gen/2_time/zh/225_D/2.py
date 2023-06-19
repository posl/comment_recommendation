def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]
