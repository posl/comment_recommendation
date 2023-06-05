def main():
    # 读取输入
    A,B = map(int,input().split())
    # print("A = ",A," B = ",B)
    # 判断是否能得到B
    if A <= B <= A * 6:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()