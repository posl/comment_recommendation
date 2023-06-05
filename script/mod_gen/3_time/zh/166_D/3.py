def main():
    # 读取输入
    x = int(input())
    # 从-200到200遍历A
    for a in range(-200, 200):
        # 从-200到200遍历B
        for b in range(-200, 200):
            # 如果A的5次方-B的5次方等于X
            if a ** 5 - b ** 5 == x:
                # 输出A和B
                print(a, b)
                # 退出程序
                exit()

if __name__ == '__main__':
    main()