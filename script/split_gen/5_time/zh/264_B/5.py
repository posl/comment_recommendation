def main():
    # 读取输入
    a = input()
    # 用空格分割
    b = a.split()
    # 转换成整数
    c = [int(i) for i in b]
    # print(c)
    # 读取行数
    R = c[0]
    # 读取列数
    C = c[1]
    # print(R)
    # print(C)
    # 判断
    if R % 2 == 0:
        if C % 2 == 0:
            print("黑色")
        else:
            print("白色")
    else:
        if C % 2 == 0:
            print("白色")
        else:
            print("黑色")
main()
