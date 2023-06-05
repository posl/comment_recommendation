def search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = int((left + right)/2)
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
