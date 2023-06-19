def root(x):
    if par[x]==x:
        return x
    else:
        par[x]=root(par[x])
        return par[x]
