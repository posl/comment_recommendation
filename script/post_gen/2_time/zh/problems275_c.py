Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d,e,f = map(int, input().split())
    if a*b*c >= d*e*f:
        print((a*b*c-d*e*f) % 998244353)
    else:
        print((d*e*f-a*b*c) % 998244353)

=======
Suggestion 2

def main():
    # 读取输入
    line = input()
    # 用空格分隔输入
    A, B, C, D, E, F = map(int, line.split())
    # 计算结果
    result = A * B * C - D * E * F
    # 打印结果
    print(result % 998244353)

=======
Suggestion 3

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 4

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

=======
Suggestion 5

def problems275_b():
    pass

=======
Suggestion 6

def problem275_b():
    a,b,c,d,e,f = map(int,input().split())
    if a*b*c >= d*e*f:
        print((a*b*c-d*e*f)%998244353)
    else:
        print(0)

=======
Suggestion 7

def main():
    A, B, C, D, E, F = map(int, input().split())
    #print(A, B, C, D, E, F)
    #print(A*B*C, D*E*F)
    if A*B*C >= D*E*F:
        print((A*B*C - D*E*F) % 998244353)
    else:
        print(0)

=======
Suggestion 8

def main():
    # 输入
    A, B, C, D, E, F = map(int, input().split())

    # 乘法的结果
    ABC = A * B * C
    DEF = D * E * F

    # 乘法的结果对998244353取模
    ABC = ABC % 998244353
    DEF = DEF % 998244353

    # 输出
    print((ABC - DEF) % 998244353)
