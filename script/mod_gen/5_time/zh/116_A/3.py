def main():
    # 读入三角形的三条边
    a, b, c = map(int, input().split())
    # 计算三角形的面积
    s = (a * b) // 2
    # 打印输出
    print(s)

if __name__ == '__main__':
    main()