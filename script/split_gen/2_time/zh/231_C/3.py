def binary_search(x, a):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid
    return left
