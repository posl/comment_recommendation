def main():
    # 读取输入
    a = input()
    # 将输入的数字分割成字符串列表
    a_list = a.split()
    # 将字符串列表转化成数字列表
    a_list = [int(i) for i in a_list]
    # 将数字列表排序
    a_list.sort()
    # 将数字列表变成字符串
    a_list = [str(i) for i in a_list]
    # 将数字列表拼接成字符串
    a = "".join(a_list)
    # 判断是否为等差数列
    if a == "135":
        print("Yes")
    elif a == "555":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()