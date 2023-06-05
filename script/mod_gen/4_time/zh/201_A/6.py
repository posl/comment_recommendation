def main():
    # 获取输入
    line = input()
    # 用空格分隔输入的三个数字
    A = line.split(" ")
    # 将字符串转换为整数
    A = [int(s) for s in A]
    # 排序
    A.sort()
    # 如果A_3-A_2=A_2-A_1，则打印“Yes”，否则打印“No”
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()