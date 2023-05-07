def main():
    #入力
    N = int(input())
    S = [input() for i in range(N)]
    #辞書型にして集計
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
    #最大値を求める
    max = 0
    for i in D.values():
        if i > max:
            max = i
    #最大値と一致するものを表示
    for i in D.keys():
        if D[i] == max:
            print(i)

if __name__ == '__main__':
    main()