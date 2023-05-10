def find_set(x):
    if x != par[x]:
        par[x] = find_set(par[x])
    return par[x]

if __name__ == '__main__':
    find_set()