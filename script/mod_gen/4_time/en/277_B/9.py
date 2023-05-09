def check_cards(cards):
    if len(cards) != len(set(cards)):
        return False
    else:
        return True

if __name__ == '__main__':
    check_cards()