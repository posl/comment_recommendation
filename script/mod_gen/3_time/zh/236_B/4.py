def find_lost_card(n, cards):
    cards.sort()
    for i in range(0, len(cards), 2):
        if cards[i] != cards[i+1]:
            return cards[i]

if __name__ == '__main__':
    find_lost_card()