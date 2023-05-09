def check_hand(hand):
    suits = []
    cards = []
    for card in hand:
        suits.append(card[0])
        cards.append(card[1])
    if len(set(suits)) != 1:
        return False
    if len(set(cards)) != 5:
        return False
    if set(cards) == set(['A', 'T', 'J', 'Q', 'K']):
        return True
    if set(cards) == set(['A', '2', '3', '4', '5']):
        return True
    if set(cards) == set(['2', '3', '4', '5', '6']):
        return True
    if set(cards) == set(['3', '4', '5', '6', '7']):
        return True
    if set(cards) == set(['4', '5', '6', '7', '8']):
        return True
    if set(cards) == set(['5', '6', '7', '8', '9']):
        return True
    if set(cards) == set(['6', '7', '8', '9', 'T']):
        return True
    if set(cards) == set(['7', '8', '9', 'T', 'J']):
        return True
    if set(cards) == set(['8', '9', 'T', 'J', 'Q']):
        return True
    if set(cards) == set(['9', 'T', 'J', 'Q', 'K']):
        return True
    if set(cards) == set(['T', 'J', 'Q', 'K', 'A']):
        return True
    if set(cards) == set(['J', 'Q', 'K', 'A', '2']):
        return True
    if set(cards) == set(['Q', 'K', 'A', '2', '3']):
        return True
    if set(cards) == set(['K', 'A', '2', '3', '4']):
        return True
    return False

if __name__ == '__main__':
    check_hand()