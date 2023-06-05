def count_higher_than_x(a, x):
    a.sort()
    count = 0
    for i in range(len(a)):
        if a[i] >= x:
            count += 1
    return count
