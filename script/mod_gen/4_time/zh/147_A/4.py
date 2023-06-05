def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())
    # 判断是否bust
    if a1 + a2 + a3 >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()