def findPath(towns, start, k):
    if k == 0:
        return start
    else:
        return findPath(towns, towns[start-1], k-1)
