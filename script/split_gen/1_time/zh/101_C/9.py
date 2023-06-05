def get_min(a):
    min = a[0]
    for i in range(1, len(a)):
        if a[i] < min:
            min = a[i]
    return min
