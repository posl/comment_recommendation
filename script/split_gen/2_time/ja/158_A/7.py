def main():
    # 入力
    S = input()
    # 出力
    if S[0] == S[1]:
        print("No")
    elif S[1] == S[2]:
        print("No")
    elif S[2] == S[0]:
        print("No")
    else:
        print("Yes")
