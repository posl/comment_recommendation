def main():
    # 输入
    C = input()
    # 处理
    if C[0] == C[1] == C[2]:
        result = "Won"
    else:
        result = "Lost"
    # 输出
    print(result)
