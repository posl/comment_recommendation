def main():
    # 入力
    S = input()
    # Sの文字数を取得
    S_len = len(S)
    # Sの先頭と末尾の文字を取得
    S_head = S[0]
    S_tail = S[-1]
    # Sの先頭と末尾が英大文字か判定
    if S_head.isupper() and S_tail.isupper():
        # Sの先頭と末尾以外の文字列を取得
        S_mid = S[1:-1]
        # Sの先頭と末尾以外の文字列の文字数を取得
        S_mid_len = len(S_mid)
        # Sの先頭と末尾以外の文字列が整数か判定
        if S_mid_len == 6 and S_mid.isdigit():
            print("Yes")
        else:
            print("No")
    else:
        print("No")
