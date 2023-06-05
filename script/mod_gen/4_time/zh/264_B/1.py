def main():
    # 读取输入
    r, c = map(int, input().split())
    # 判断是否为黑色
    if (r+c)%2 == 0:
        print("黑色")
    else:
        print("白色")

if __name__ == '__main__':
    main()