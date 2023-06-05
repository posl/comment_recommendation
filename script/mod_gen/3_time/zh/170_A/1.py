def main():
    # 读入数据
    x = input().split()
    # 处理数据
    for i in range(0, 5):
        if x[i] == '0':
            print(i+1)
            break

if __name__ == '__main__':
    main()