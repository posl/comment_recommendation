def find_missing_card(n, cards):
    cards.sort()
    for i in range(0, len(cards), 2):
        if cards[i] != cards[i+1]:
            return cards[i]
    return cards[-1]

if __name__ == '__main__':
    find_missing_card()