def main():
    # 读取数据
    data = []
    for i in range(9):
        data.append(list(input()))
    # print(data)
    # 统计棋子个数
    count = 0
    for i in range(9):
        for j in range(9):
            if data[i][j] == "#":
                count += 1
    # print(count)
    # 统计顶点个数
    count2 = 0
    for i in range(9):
        for j in range(9):
            if i < 8 and j < 8:
                if data[i][j] == "#" and data[i + 1][j] == "#" and data[i][j + 1] == "#" and data[i + 1][j + 1] == "#":
                    count2 += 1
    # print(count2)
    # 输出结果
    print(count - count2)

if __name__ == '__main__':
    main()