def main():
    # 读入S和T
    S = input()
    T = input()
    # 请在此添加您的代码
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()