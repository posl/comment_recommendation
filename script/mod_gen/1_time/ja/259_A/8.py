def main():
    #入力
    N, M, X, T, D = map(int, input().split())
    #M歳の誕生日の時の身長を求める
    H = T + D * (M - X)
    #M歳の誕生日の時の身長がN歳の誕生日の時の身長よりも低い場合、
    #N歳の誕生日の時の身長を出力する
    if H < T + D * (N - X):
        print(T + D * (N - X))
    #M歳の誕生日の時の身長がN歳の誕生日の時の身長よりも高い場合、
    #M歳の誕生日の時の身長を出力する
    else:
        print(H)

if __name__ == '__main__':
    main()