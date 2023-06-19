def main():
    # 读入数据
    # 由于输入数据是一行，所以使用input()函数
    # input()函数会读入一行数据，并将末尾的换行符去掉
    # 然后，将这行数据赋值给变量line
    line = input()
    # 使用空格分割line
    # 分割后，line是一个列表，列表中的每个元素都是字符串
    # 使用map()函数，将列表中的每个元素转换为整数
    a, b, c = map(int, line.split())
    # 计算三角形面积
    s = a * b / 2
    # 打印结果
    print(int(s))
main()
