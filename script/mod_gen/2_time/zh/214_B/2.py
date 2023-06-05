def main():
    # 读入一个整数
    n = int(input())
    # 判断
    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)

if __name__ == '__main__':
    main()