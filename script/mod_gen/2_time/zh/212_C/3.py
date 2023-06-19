def min_diff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    min_diff = abs(arr1[i] - arr2[j])
    while i < len(arr1) and j < len(arr2):
        min_diff = min(min_diff, abs(arr1[i] - arr2[j]))
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return min_diff

if __name__ == '__main__':
    min_diff()