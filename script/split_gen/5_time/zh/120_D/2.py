def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]
