def main():
    S = input()
    T = input()
    
    # スタックを用いた解法
    # スタックにTの文字を順番に積み、Sの文字とスタックの文字を比較する
    # Sの文字とスタックの文字が一致した場合はスタックから一つ文字を取り出す
    # Sの文字とスタックの文字が一致しない場合はスタックにTの文字を積む
    # スタックの文字を全て取り出すまでにSの文字がなくなった場合はNoを出力
    # スタックの文字を全て取り出すまでにSの文字がなくならなかった場合はNoを出力
    # スタックの文字を全て取り出した場合はYesを出力
    stack = []
    for i in range(len(T)):
        stack.append(T[i])
    
    s_index = 0
    while stack:
        if s_index >= len(S):
            print("No")
            return
        if S[s_index] == stack[-1]:
            stack.pop()
        else:
            stack.append(T[i])
        s_index += 1
    
    if s_index < len(S):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()