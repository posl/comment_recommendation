def findTriangleCount(arr):
    count = 0
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] != arr[j] and arr[j] != arr[k] and arr[i] != arr[k]:
                    if arr[i] + arr[j] > arr[k] and arr[j] + arr[k] > arr[i] and arr[i] + arr[k] > arr[j]:
                        count += 1
    return count

if __name__ == '__main__':
    findTriangleCount()