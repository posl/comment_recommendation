def binary_search(A, x):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= x:
            left = mid
        else:
            right = mid
    return left

if __name__ == '__main__':
    binary_search()