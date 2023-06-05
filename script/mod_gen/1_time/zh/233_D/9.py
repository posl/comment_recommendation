def subarray_sum(arr, k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                count += 1
    return count

if __name__ == '__main__':
    subarray_sum()