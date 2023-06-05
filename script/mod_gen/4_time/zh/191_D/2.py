def main():
    import sys
    import math
    # 读入数据
    data = sys.stdin.readline().strip().split()
    x, y, r = map(float, data)
    # 计算
    x1 = math.floor(x - r)
    x2 = math.ceil(x + r)
    count = 0
    for i in range(x1, x2 + 1):
        y1 = math.floor(y - math.sqrt(r * r - (i - x) * (i - x)))
        y2 = math.ceil(y + math.sqrt(r * r - (i - x) * (i - x)))
        for j in range(y1, y2 + 1):
            if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()