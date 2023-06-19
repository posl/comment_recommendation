def main():
    # 读取输入
    S = input()
    # print(S)
    # print(S[0])
    # print(S[1])
    # print(S[2])
    # print(S[3])
    # print(S[0] == S[1])
    # print(S[1] == S[2])
    # print(S[2] == S[3])
    # print(S[0] == S[1] or S[1] == S[2] or S[2] == S[3])
    # print(S[0] == S[1] and S[1] == S[2] and S[2] == S[3])
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
