def getMedian(a):
    #a.sort()
    #print(a)
    #return a[int(len(a)/2)]
    return sorted(a)[int(len(a)/2)]

if __name__ == '__main__':
    getMedian()