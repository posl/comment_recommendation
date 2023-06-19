def getMedian(arr):
    arr.sort()
    return arr[len(arr)//2]

if __name__ == '__main__':
    getMedian()