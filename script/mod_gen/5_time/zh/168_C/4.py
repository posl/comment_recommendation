def main():
    # 读入输入
    a, b, h, m = map(int, input().split())
    # 计算角度
    a_rad = 2 * 3.14159265358979323846 * (h / 12 + m / 60 / 12)
    b_rad = 2 * 3.14159265358979323846 * (m / 60)
    # 计算距离
    import math
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(a_rad - b_rad)))

if __name__ == '__main__':
    main()