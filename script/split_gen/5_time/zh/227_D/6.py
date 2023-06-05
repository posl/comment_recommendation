def get_max_project_num(n, k, a):
    a.sort()
    i = 0
    j = 0
    count = 0
    while i < n and j < n:
        if a[j] - a[i] + 1 > k:
            i += 1
        else:
            count += 1
            j += 1
    return count
