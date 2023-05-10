def get_contiguous_subsequences(a, k):
    count = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum >= k:
                count += 1
                break
    return count
