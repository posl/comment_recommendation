def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # print(N, K)
    # print(P)
    # 1からNの配列を作成
    cards = [i for i in range(1, N+1)]
    print(cards)
    # 1からNの配列をPの順番に並び替え
    cards = [cards[i-1] for i in P]
    print(cards)
    # 1からNの配列をPの順番に並び替え
    cards = [cards[i-1] for i in P]
    print(cards)

if __name__ == '__main__':
    main()