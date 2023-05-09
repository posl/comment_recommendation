def check_card(card):
    suits = ['H', 'D', 'C', 'S']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T','J','Q','K']
    if card[0] not in suits:
        return False
    if card[1] not in ranks:
        return False
    return True
