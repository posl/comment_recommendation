def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]
