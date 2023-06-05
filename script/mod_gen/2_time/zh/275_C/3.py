def problems275_b():
    #读取输入
    line = input()
    #分割输入
    line = line.split()
    #将输入的字符串转换为整数
    line = list(map(int, line))
    #将输入的整数赋值给变量
    A = line[0]
    B = line[1]
    C = line[2]
    D = line[3]
    E = line[4]
    F = line[5]
    #计算（A×B×C）-（D×E×F）除以998244353时的余数
    result = (A*B*C - D*E*F) % 998244353
    #输出结果
    print(result)

if __name__ == '__main__':
    problems275_b()