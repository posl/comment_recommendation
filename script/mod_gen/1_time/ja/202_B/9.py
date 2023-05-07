def main():
    # 入力
    S = input()
    # 処理
    S = S[::-1] # 反転
    S = S.replace('6', 'x') # 6をxに置換
    S = S.replace('9', '6') # 9を6に置換
    S = S.replace('x', '9') # xを9に置換
    # 出力
    print(S)

if __name__ == '__main__':
    main()