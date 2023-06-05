def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算结果
    if A == B:
        print(A + B)
    elif A > B:
        print(A + A - 1)
    else:
        print(B + B - 1)

if __name__ == '__main__':
    main()