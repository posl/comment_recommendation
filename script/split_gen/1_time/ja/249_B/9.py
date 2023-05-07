def main():
    # 入力
    S = input()
    # 処理
    flg = True
    for i in range(len(S)):
        if S[i].isupper():
            for j in range(len(S)):
                if S[j].islower():
                    for k in range(len(S)):
                        if S[i] == S[j] or S[i] == S[k] or S[j] == S[k]:
                            flg = False
                            break
    # 出力
    if flg:
        print("Yes")
    else:
        print("No")
