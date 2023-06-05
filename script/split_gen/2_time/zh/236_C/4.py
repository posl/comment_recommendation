def get_missing_card(n, cards):
    card_dict = {}
    for card in cards:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    for i in range(1, n + 1):
        if i not in card_dict or card_dict[i] != 4:
            return i
