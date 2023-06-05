def main():
    # 读取输入
    S = input()
    # 请在此添加您的代码
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
    return

if __name__ == '__main__':
    main()