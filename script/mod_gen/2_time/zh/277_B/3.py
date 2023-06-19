def is_valid_cards(cards):
    if len(cards) != 2:
        return False
    elif cards[0] not in "HDCS":
        return False
    elif cards[1] not in "A23456789TJQK":
        return False
    return True

if __name__ == '__main__':
    is_valid_cards()