def main():
    # 读取输入
    x = int(input())
    # 钱包里至少有一个100日元的硬币
    if x >= 100:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()