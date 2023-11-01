def main():
    # 从标准输入读取
    a, b, c, d, e, f, x = map(int, input().split())
    # 高桥和青木的位移
    t = 0
    s = 0
    # 高桥和青木的状态，0为移动，1为休息
    h = 0
    q = 0
    # 一直移动，直到高桥和青木的位移都大于等于x
    while t < x or s < x:
        # 高桥移动
        if h == 0:
            t += a
            h = 1
        # 高桥休息
        else:
            h = 0
        # 青木移动
