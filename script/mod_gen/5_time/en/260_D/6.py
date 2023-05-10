def find_smallest_greater_than_or_equal_to_x(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    return l

if __name__ == '__main__':
    find_smallest_greater_than_or_equal_to_x()