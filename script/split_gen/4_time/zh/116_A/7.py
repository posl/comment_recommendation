def main():
    # 读入数据
    line = input('请输入三角形的三边长，以空格分隔：')
    # 用空格分隔读入的数据
    line = line.split()
    # 把字符型数据转换成整数型数据
    line = [int(x) for x in line]
    # 计算三角形的面积
    area = line[0] * line[1] / 2
    # 打印结果
    print('三角形的面积是：', area)
