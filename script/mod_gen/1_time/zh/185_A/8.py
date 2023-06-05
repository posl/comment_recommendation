def main():
    # 读取输入
    A = [int(x) for x in input().split()]
    # 处理
    A.sort()
    print(A[0])

if __name__ == '__main__':
    main()