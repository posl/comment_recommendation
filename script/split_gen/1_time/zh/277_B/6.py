def check_card(card):
    if len(card) != 2:
        return False
    if card[0] not in ['H', 'D', 'C', 'S']:
        return False
    if card[1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T','J', 'Q', 'K']:
        return False
    return True
