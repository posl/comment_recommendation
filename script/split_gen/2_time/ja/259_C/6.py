def main():
    S = input()
    T = input()
    # Sの文字列の長さ
    len_s = len(S)
    # Tの文字列の長さ
    len_t = len(T)
    # Sの文字列の長さがTの文字列の長さよりも大きい場合はNoを出力
    if len_s > len_t:
        print("No")
        return
    # Sの文字列の長さがTの文字列の長さよりも小さい場合
    # Sの文字列の長さ分ループを回し、Sの文字列とTの文字列を比較
    # Sの文字列とTの文字列が一致している場合は、Sの文字列の長さを1増やす
    # Sの文字列とTの文字列が一致していない場合は、Sの文字列の長さを1減らす
    # Sの文字列の長さがTの文字列の長さになった場合は、Yesを出力
    # Sの文字列の長さがTの文字列の長さにならなかった場合は、Noを出力
    for i in range(len_t):
        if S == T[i:i+len_s]:
            print("Yes")
            return
    print("No")
