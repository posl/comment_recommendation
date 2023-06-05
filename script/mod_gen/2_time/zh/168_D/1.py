def clock():
    import math
    import sys
    # 读取输入
    a, b, h, m = map(int, sys.stdin.readline().strip().split())
    # 计算角度
    angle = abs(30 * h + 0.5 * m - 6 * m)
    # 计算距离
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))
    # 打印答案
    print(ans)

if __name__ == '__main__':
    clock()