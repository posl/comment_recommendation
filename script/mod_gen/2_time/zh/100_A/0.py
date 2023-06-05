def main():
    # 读取输入
    A, B = map(int, input().split())
    # 判断是否满足条件
    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()