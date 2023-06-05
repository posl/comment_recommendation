def main():
    # 读入S
    S = input()
    # 读入T
    T = input()
    # 预测正确的天数
    correct = 0
    # 预测正确的天数
    for i in range(3):
        if S[i] == T[i]:
            correct += 1
    # 打印预测正确的天数
    print(correct)
