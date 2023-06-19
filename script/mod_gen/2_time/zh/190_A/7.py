def main():
    # 读取数据
    a, b, c = map(int, input().split())
    # 判断谁先吃
    if c == 0:
        # 先吃的是高桥
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        # 先吃的是青木
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

if __name__ == '__main__':
    main()