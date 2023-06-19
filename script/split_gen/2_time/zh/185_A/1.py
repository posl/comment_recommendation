def main():
    # 读取输入
    a = input()
    # 分割输入
    a_list = a.split(" ")
    # 把输入转换成整数
    for i in range(len(a_list)):
        a_list[i] = int(a_list[i])
    # 排序
    a_list.sort()
    # 计算
    count = 0
    for i in range(len(a_list)):
        if a_list[i] % 100 == 0:
            count += 1
    # 输出
    print(count)
