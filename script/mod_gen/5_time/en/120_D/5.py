def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

if __name__ == '__main__':
    find()