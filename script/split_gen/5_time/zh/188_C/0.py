def get_second_place(N, A):
    # 二分查找
    def binary_search(A, l, r):
        if l == r:
            return A[l]
        else:
            mid = (l + r) // 2
            left = binary_search(A, l, mid)
            right = binary_search(A, mid + 1, r)
            if left > right:
                return left
            else:
                return right
    # 从小到大排序
    A.sort()
    # 二分查找
    second_place = binary_search(A, 0, len(A) - 1)
    return second_place
