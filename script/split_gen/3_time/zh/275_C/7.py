def main():
    # 读取输入
    input = []
    for i in range(9):
        input.append(input())
    # 处理
    count = 0
    for i in range(9):
        for j in range(9):
            if input[i][j] == '#':
                count += 1
    # 输出结果
    print(count)
main()
