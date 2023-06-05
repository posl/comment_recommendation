def main():
    # 读取标准输入
    # 读取第一行的n
    q = int(input())
    # 读取每一行
    for i in range(q):
        # 读取每一行
        line = input().split()
        # 读取每一行
        if line[0] == "1":
            num = int(line[1])
            print(num)
        elif line[0] == "2":
            num = int(line[1])
            print(num)
        elif line[0] == "3":
            print(1)

if __name__ == '__main__':
    main()