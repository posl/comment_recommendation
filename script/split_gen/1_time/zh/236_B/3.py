def find_lost_card(n, cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    for i in range(1, n+1):
        if i not in card_count or card_count[i] != 4:
            return i
