def findPath(towns, start, k):
    if k == 0:
        return start
    else:
        return findPath(towns, towns[start-1], k-1)

if __name__ == '__main__':
    findPath()