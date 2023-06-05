def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

if __name__ == '__main__':
    main()