def main():
    # 输入数据
    n = int(input())
    t = input()
    # 初始化
    x = 0
    y = 0
    direction = 0
    # 处理数据
    for i in range(n):
        if t[i] == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            else:
                y += 1
        else:
            direction += 1
            if direction == 4:
                direction = 0
    # 输出结果
    print(x, y)

if __name__ == '__main__':
    main()