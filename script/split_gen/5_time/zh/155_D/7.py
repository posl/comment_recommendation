def main():
    # 读入数据
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 二分查找
    # 1. 二分查找的对象是乘积的值
    # 2. 二分查找的上下限是乘积的下限和上限
    # 3. 二分查找的计算方法是计算小于等于该乘积的个数
    # 4. 二分查找的结束条件是下限和上限相等
    # 5. 二分查找的结果是上限
    A.sort()
    low = A[0] * A[1]
    high = A[-1] * A[-2]
    while low < high:
        mid = (low + high) // 2
        # 计算小于等于该乘积的个数
        count = 0
        left = 0
        right = N - 1
        if A[left] * A[right] <= mid:
            count += right - left
        else:
            while left < right:
                if A[left] * A[right] <= mid:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        # 比较个数与 K 的大小
        if count < K:
            low = mid + 1
        else:
            high = mid
    print(low)
