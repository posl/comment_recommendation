def findRoots(n, m, edges):
    roots = [i for i in range(n)]
    for edge in edges:
        roots[edge[1]] = roots[edge[0]]
    return roots

if __name__ == '__main__':
    findRoots()