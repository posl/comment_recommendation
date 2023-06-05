def main():
    #读取输入
    inputs = input().split()
    #将读取的输入转换为整数
    A = int(inputs[0])
    B = int(inputs[1])
    #计算A+B
    sum = A + B
    #如果sum小于10^18，输出Easy
    if sum < 10**18:
        print("Easy")
    #如果sum大于等于10^18，输出Hard
    else:
        print("Hard")

if __name__ == '__main__':
    main()