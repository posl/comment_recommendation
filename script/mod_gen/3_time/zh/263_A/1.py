def main():
    # 读入数据
    line = input()
    # 分割数据
    line = line.split()
    # 数据转换
    line = list(map(int, line))
    # 排序
    line.sort()
    # 判断是否为满堂红
    if line[0] == line[1] and line[3] == line[4] and (line[0] != line[3] or line[0] != line[4]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()