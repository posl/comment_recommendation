def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    if len(set(cards)) == n:
        for card in cards:
            if card[0] not in ['H','D','C','S']:
                print('No')
                return
            if card[1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
                print('No')
                return
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()