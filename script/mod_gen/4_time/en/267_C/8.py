def max_subarray_sum(a, m):
    max_sum = 0
    for i in range(len(a) - m + 1):
        subarray_sum = 0
        for j in range(i, i + m):
            subarray_sum += a[j] * (j - i + 1)
        max_sum = max(max_sum, subarray_sum)
    return max_sum

if __name__ == '__main__':
    max_subarray_sum()