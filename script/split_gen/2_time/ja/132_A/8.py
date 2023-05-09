def main():
    S = input()
    if len(S) != 4:
        print("入力が不正です。")
        return
    elif S[0] == S[1] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")
