def main():
    # 读取输入
    S = input()
    # 计算
    # 由于S是4位数，因此只需要比较第1位和第2位，第2位和第3位，第3位和第4位
    # 如果有相同的，就打印Bad，然后退出
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
        return
    # 如果没有相同的，就打印Good
    print("Good")

if __name__ == '__main__':
    main()