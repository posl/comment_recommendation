def main():
    print("请输入一个半径：")
    r = int(input())
    if r < 1 or r > 100:
        print("请输入一个1-100的整数")
        return
    s = 3 * r * r
    print("正十二边形的面积是：{0}".format(s))
