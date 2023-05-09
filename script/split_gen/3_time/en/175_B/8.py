def count_triangles(arr):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] > arr[k]:
                    count += 1
                else:
                    break
    return count
