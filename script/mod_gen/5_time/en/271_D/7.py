def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int, input().split())))
    for i in range(2**N):
        tmp = S
        tmp_cards = []
        for j in range(N):
            if (i >> j) & 1:
                tmp -= cards[j][0]
                tmp_cards.append('H')
            else:
                tmp -= cards[j][1]
                tmp_cards.append('T')
        if tmp == 0:
            print('Yes')
            print(''.join(tmp_cards))
            exit()
    print('No')

if __name__ == '__main__':
    main()