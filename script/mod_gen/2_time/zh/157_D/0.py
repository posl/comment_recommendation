def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

if __name__ == '__main__':
    find()