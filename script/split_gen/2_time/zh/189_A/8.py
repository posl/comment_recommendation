def main():
    #输入
    C_1, C_2, C_3 = input().split()
    #处理
    if C_1 == C_2 == C_3:
        result = "Won"
    else:
        result = "Lost"
    #输出
    print(result)
