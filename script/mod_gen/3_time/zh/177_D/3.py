def find(x):
    if(x != p[x]):
        p[x] = find(p[x])
    return p[x]

if __name__ == '__main__':
    find()