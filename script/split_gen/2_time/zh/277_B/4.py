def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    if len(cards) != len(set(cards)):
        print('No')
    else:
        for card in cards:
            if card[0] not in ['H','D','C','S']:
                print('No')
                break
            if card[1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
                print('No')
                break
        else:
            print('Yes')
