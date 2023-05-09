def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # !aとaのペアを作成する
    # その際、aが存在しない場合は空文字列を代入する
    S_pair = {}
    for s in S:
        if s[0] == "!":
            S_pair[s[1:]] = s
        else:
            S_pair[s] = ""
    # S_pairの中で、空文字列を持つキーを探す
    for k, v in S_pair.items():
        if v == "":
            continue
        else:
            if k in S_pair:
                print(k)
                return
    print("satisfiable")

if __name__ == '__main__':
    main()