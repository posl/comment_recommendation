def binary_search(target, array):
    """
    二分法查找
    :param target: 目标值
    :param array: 有序数组
    :return: 目标值在数组中的索引
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    binary_search()