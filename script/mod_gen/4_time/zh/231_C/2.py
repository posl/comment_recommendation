def binary_search(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return right

if __name__ == '__main__':
    binary_search()