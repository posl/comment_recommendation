def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 检查是否存在一对不能直接通信的天线
    if e - a > k:
        print(":(")
    else:
        print("Yay!")

if __name__ == '__main__':
    main()