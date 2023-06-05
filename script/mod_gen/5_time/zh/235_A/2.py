def main():
    # 读取输入
    abc = input()
    # 计算abc+bca+cab
    bca = int(abc[1]+abc[2]+abc[0])
    cab = int(abc[2]+abc[0]+abc[1])
    sum = int(abc)+bca+cab
    # 输出结果
    print(sum)
main()
