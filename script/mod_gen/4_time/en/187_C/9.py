def main():
    #入力
    N = int(input())
    S = [input() for _ in range(N)]
    #重複を削除
    S = list(set(S))
    #出力
    for i in range(len(S)):
        if "!" + S[i] in S:
            print(S[i])
            exit()
    print("satisfiable")

if __name__ == '__main__':
    main()