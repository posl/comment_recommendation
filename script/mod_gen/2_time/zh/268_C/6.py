def main():
    # 读取输入
    s = input()
    t = input()
    # 检查
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()