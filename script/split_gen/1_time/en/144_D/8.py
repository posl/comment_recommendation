def main():
    import math
    a, b, x = map(int, input().split())
    if x > a**2 * b / 2:
        # 三角形
        x = a**2 * b - x
        h = x / (a**2)
        rad = math.atan(2 * h / a)
    else:
        # 二等辺三角形
        h = x * 2 / (a**2)
        rad = math.atan(a / 2 / h)
    print(math.degrees(rad))
