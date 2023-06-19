def main():
    # 读取输入
    A = input().split()
    # 是否可以重新排列A的元素成为算术序列
    if int(A[2]) - int(A[1]) == int(A[1]) - int(A[0]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()