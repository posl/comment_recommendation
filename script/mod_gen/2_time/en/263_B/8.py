def findParent(parents, p):
    if parents[p] == p:
        return p
    else:
        return findParent(parents, parents[p])

if __name__ == '__main__':
    findParent()