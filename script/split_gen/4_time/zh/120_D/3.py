def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
