def main():
    # 读取输入
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    d = int(line[3])
    # 模拟战斗
    while True:
        c = c - b
        if c <= 0:
            print("Yes")
            break
        a = a - d
        if a <= 0:
            print("No")
            break

if __name__ == '__main__':
    main()