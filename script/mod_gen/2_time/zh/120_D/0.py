def find_parent(x, parents):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_parent(parents[x], parents)
        return parents[x]

if __name__ == '__main__':
    find_parent()