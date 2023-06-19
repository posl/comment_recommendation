def main():
    # 读取输入
    A, B, C, D = map(int, input().split())
    # 高桥和青木轮流攻击
    while True:
        # 高桥攻击青木
        C -= B
        # 青木判断输赢
        if C <= 0:
            print("Yes")
            break
        # 青木攻击高桥
        A -= D
        # 高桥判断输赢
        if A <= 0:
            print("No")
            break

if __name__ == '__main__':
    main()