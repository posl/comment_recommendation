def find_kth(a, x, k):
    count = 1
    for i in range(len(a)):
        if a[i] == x:
            if count == k:
                return i+1
            count += 1
    return -1
