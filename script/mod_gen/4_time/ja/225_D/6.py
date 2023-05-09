def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

if __name__ == '__main__':
    find()