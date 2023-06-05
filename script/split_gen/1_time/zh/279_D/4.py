def main():
    # 读入数据
    a, b = map(int, input().split())
    # 二分查找
    # 1. 左边界：不进行操作时所需时间
    # 2. 右边界：进行操作无限次时所需时间
    # 3. 判断中间值所需时间
    # 4. 判断中间值的下一个值所需时间
    # 5. 重复 3、4
    # 6. 返回左边界
    left = 0
    right = 1e18
    while right - left > 1e-7:
        mid = (left + right) / 2
        if mid + a / (b * mid ** 0.5) < mid + 1e-7 + a / (b * (mid + 1e-7) ** 0.5):
            right = mid
        else:
            left = mid
    print(left)
