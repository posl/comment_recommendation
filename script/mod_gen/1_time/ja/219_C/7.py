def main():
    #入力
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    #処理
    #アルファベット順に並べ替える
    S.sort(key=lambda x: [X.index(c) for c in x])
    #出力
    for i in range(N):
        print(S[i])

if __name__ == '__main__':
    main()