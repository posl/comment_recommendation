def main():
    # 读取输入
    lines = []
    for i in range(10):
        lines.append(input())
    # print(lines)
    # 寻找第一个字符
    for i in range(10):
        if lines[i].find("#") != -1:
            first = i
            break
    # 寻找最后一个字符
    for i in range(9, -1, -1):
        if lines[i].find("#") != -1:
            last = i
            break
    # 寻找第一个行
    for i in range(10):
        if lines[i][0] == "#":
            firstCol = i
            break
    # 寻找最后一行
    for i in range(9, -1, -1):
        if lines[i][9] == "#":
            lastCol = i
            break
    print(first+1, last+1)
    print(firstCol+1, lastCol+1)

if __name__ == '__main__':
    main()