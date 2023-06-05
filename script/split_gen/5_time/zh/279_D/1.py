def main():
    # 读入数据
    a, b = map(int, input().split())
    # 二分法求解
    left = 0
    right = 10 ** 18
    while right - left > 10 ** (-6):
        mid = (left + right) / 2
        if mid + a / (b * mid ** 0.5) < mid + a / ((b + 1) * (mid + 1) ** 0.5):
            right = mid
        else:
            left = mid
    print(left + a / (b * left ** 0.5))
