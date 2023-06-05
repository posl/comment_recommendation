def findMedian(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    if len(arr) % 2 == 0:
        return arr[len(arr) // 2]
    else:
        return arr[(len(arr) - 1) // 2]

if __name__ == '__main__':
    findMedian()