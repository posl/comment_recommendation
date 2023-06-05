def main():
    # 天气预报
    S = input()
    # 实际天气
    T = input()
    # 预测正确的天数
    correct_days = 0
    for i in range(3):
        if S[i] == T[i]:
            correct_days += 1
    print(correct_days)
