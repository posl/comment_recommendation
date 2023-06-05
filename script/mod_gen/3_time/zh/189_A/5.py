def main():
    # 从标准输入读取
    str = input()
    # 判断是否是赢了
    if str[0] == str[1] and str[1] == str[2]:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    main()