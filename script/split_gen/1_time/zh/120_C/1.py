def main():
    # 读入数据
    str = input()
    # 计算数据
    count0 = 0
    count1 = 0
    for i in range(len(str)):
        if str[i] == '0':
            count0 += 1
        else:
            count1 += 1
    # 输出结果
    print(min(count0, count1) * 2)
