def parent(x):
    if par[x] == x:
        return x
    else:
        par[x] = parent(par[x])
        return par[x]

if __name__ == '__main__':
    parent()