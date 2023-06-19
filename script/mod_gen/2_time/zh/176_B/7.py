def main():
    # 读入数据
    N = input()
    # 处理数据
    sum = 0
    for i in N:
        sum += int(i)
    # 输出结果
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()