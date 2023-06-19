def findRoot(roots, i):
    if roots[i] == i:
        return i
    else:
        roots[i] = findRoot(roots, roots[i])
        return roots[i]

if __name__ == '__main__':
    findRoot()