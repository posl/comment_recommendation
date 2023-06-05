def main():
    # 读取输入
    k, x = map(int, input().split())
    # 求解
    if 500 * k >= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()