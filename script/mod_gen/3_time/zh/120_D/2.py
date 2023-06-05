def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

if __name__ == '__main__':
    find()