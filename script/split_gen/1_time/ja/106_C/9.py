def main():
    S = input()
    K = int(input())
    # print(S,K)
    # 1日後の文字列を作る
    S2 = ""
    for i in range(len(S)):
        s = S[i]
        if s == "1":
            S2 += "1"
        else:
            S2 += s * int(s)
    # 2日後の文字列を作る
    S3 = ""
    for i in range(len(S2)):
        s = S2[i]
        if s == "1":
            S3 += "1"
        else:
            S3 += s * int(s)
    # 3日後の文字列を作る
    S4 = ""
    for i in range(len(S3)):
        s = S3[i]
        if s == "1":
            S4 += "1"
        else:
            S4 += s * int(s)
    # 5000兆日後の文字列を作る
    S5000 = ""
    for i in range(len(S4)):
        s = S4[i]
        if s == "1":
            S5000 += "1"
        else:
            S5000 += s * int(s)
    # 5000兆日後の文字列のK文字目を出力
    print(S5000[K-1])
