def main():
    # 读取输入
    S = input()
    # 判断是否有两个连续的数字是相同的
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
