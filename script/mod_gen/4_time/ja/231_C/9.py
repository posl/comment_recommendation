def binary_search(array, target):
    """二分探索の実装
    Args:
        array (list): 検索対象の配列
        target (int): 検索する値
    Returns:
        int: 検索結果のインデックス
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    binary_search()