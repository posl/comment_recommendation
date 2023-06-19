def main():
    # 读取输入
    k = int(input())
    s = input()
    # 请在此添加代码
    if k < len(s):
        print(s[0:k] + "...")
    else:
        print(s)

if __name__ == '__main__':
    main()