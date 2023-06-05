def main():
    # 读取输入
    s = input()
    # 判断是否胜利
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    main()