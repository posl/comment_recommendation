def find(x):
    global par
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
