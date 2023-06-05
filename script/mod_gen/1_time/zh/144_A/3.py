def main():
    # 读取输入
    A, B = map(int, input().split())
    # 判断A, B是否在1到20之间
    if 1 <= A <= 20 and 1 <= B <= 20:
        # 计算A*B
        print(A * B)
    else:
        print(-1)

if __name__ == '__main__':
    main()