def main():
    # 读取输入
    A, B = map(int, input().split())
    # 输出结果
    if 0 < A and B == 0:
        print("Gold")
    elif A == 0 and 0 < B:
        print("Silver")

if __name__ == '__main__':
    main()