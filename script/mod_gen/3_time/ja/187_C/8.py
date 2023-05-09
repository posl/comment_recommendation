def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #重複を除く
    S = list(set(S))
    #先頭に ! が付いているかどうかで、リストを分ける
    S_with_exclamation = [s for s in S if s[0] == "!"]
    S_without_exclamation = [s for s in S if s[0] != "!"]
    #先頭に ! が付いているものと付いていないものの重複を取り除いているので、
    #重複があれば不満な文字列が存在する
    for s in S_with_exclamation:
        if s[1:] in S_without_exclamation:
            print(s[1:])
            return
    print("satisfiable")
    return

if __name__ == '__main__':
    main()