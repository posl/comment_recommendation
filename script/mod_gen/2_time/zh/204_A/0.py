def getMedian(arr):
    arr.sort()
    l = len(arr)
    if l%2 == 0:
        return arr[l/2-1]
    else:
        return arr[(l+1)/2-1]

if __name__ == '__main__':
    getMedian()