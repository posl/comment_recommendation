def main():
    S = input()
    N = len(S)
    # 0で塗りつぶした場合の塗り替え回数
    cnt1 = 0
    # 1で塗りつぶした場合の塗り替え回数
    cnt2 = 0
    # 0で塗りつぶした場合の塗り替え回数をカウント
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '1':
                cnt1 += 1
        else:
            if S[i] == '0':
                cnt1 += 1
    # 1で塗りつぶした場合の塗り替え回数をカウント
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                cnt2 += 1
        else:
            if S[i] == '1':
                cnt2 += 1
    # 0で塗りつぶした場合と1で塗りつぶした場合の塗り替え回数の小さい方を出力
    print(min(cnt1, cnt2))

if __name__ == '__main__':
    main()