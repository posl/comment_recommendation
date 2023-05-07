def main():
    #入力
    A, B, C, D, E = map(int, input().split())
    #print(A, B, C, D, E)
    #リストに値を格納
    L = [A, B, C, D, E]
    #print(L)
    #リストの要素の個数を出力
    print(len(set(L)))

if __name__ == '__main__':
    main()