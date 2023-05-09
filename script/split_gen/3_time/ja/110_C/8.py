def main():
    S = input()
    T = input()
    #Sの文字をTの文字に変換する辞書を作成
    S_to_T = {}
    T_to_S = {}
    for i in range(len(S)):
        if S[i] in S_to_T:
            if S_to_T[S[i]] != T[i]:
                print("No")
                return
        else:
            S_to_T[S[i]] = T[i]
        if T[i] in T_to_S:
            if T_to_S[T[i]] != S[i]:
                print("No")
                return
        else:
            T_to_S[T[i]] = S[i]
    print("Yes")
    return
