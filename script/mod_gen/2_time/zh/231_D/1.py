def binary_search(x, array, left, right):
    if left == right:
        return left
    if left + 1 == right:
        if array[left] >= x:
            return left
        else:
            return right
    middle = (left + right) // 2
    if array[middle] >= x:
        return binary_search(x, array, left, middle)
    else:
        return binary_search(x, array, middle, right)

if __name__ == '__main__':
    binary_search()