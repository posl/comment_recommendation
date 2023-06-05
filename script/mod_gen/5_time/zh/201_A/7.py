def main():
    # 读入输入
    A = list(map(int, input().split()))
    # 排序
    A.sort()
    # 判断
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()