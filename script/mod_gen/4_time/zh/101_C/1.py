def getMinOpNum(n, k, a):
    minNum = min(a)
    minNumIndex = a.index(minNum)
    if minNumIndex < k-1:
        return minNumIndex + 1 + getMinOpNum(n, k, a[minNumIndex+1:])
    elif minNumIndex > n - k:
        return n - minNumIndex + getMinOpNum(n, k, a[:minNumIndex])
    else:
        return minNumIndex + 1

if __name__ == '__main__':
    getMinOpNum()