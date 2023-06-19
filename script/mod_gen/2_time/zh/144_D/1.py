def solve(a, b, x):
    # 二分法
    # 水的体积
    water = x / a
    # 水的高度
    h = water / a * 2
    # 二分法
    left = 0
    right = 90
    while right - left > 0.0000000001:
        mid = (left + right) / 2
        # 角度转弧度
        rad = mid * 3.14159265358979323846264338327950288 / 180
        # 水的高度
        h = b * math.tan(rad)
        # 水的体积
        water = a * a * b - a * a * h / 2
        # 比较
        if water > x:
            right = mid
        else:
            left = mid
    return mid
a, b, x = map(int, input().split())
print(solve(a, b, x))
