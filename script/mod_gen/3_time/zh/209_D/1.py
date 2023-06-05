def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

if __name__ == '__main__':
    find()