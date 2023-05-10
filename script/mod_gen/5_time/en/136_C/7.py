def isNonDecreasing(arr):
    if len(arr) == 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

if __name__ == '__main__':
    isNonDecreasing()