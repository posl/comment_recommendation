def main():
    # 读取输入
    S = input()
    # 初始化变量
    num = 0
    # 计算
    for i in range(len(S)):
        if S[i] == '+':
            num += 1
        else:
            num -= 1
    # 输出结果
    print(num)
