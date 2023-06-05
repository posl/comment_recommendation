def main():
    # 输入
    a, b, c = map(int, input().split())
    # 处理
    if c == 0:
        # 高桥先做
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        # 青木先做
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

if __name__ == '__main__':
    main()