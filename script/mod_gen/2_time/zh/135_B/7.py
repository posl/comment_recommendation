def checkSort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

if __name__ == '__main__':
    checkSort()