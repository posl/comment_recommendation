def main():
    # 读取输入
    X = int(input())
    # 判断
    if X >= 100 and X <= 1000:
        if X % 100 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()