def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

if __name__ == '__main__':
    find()