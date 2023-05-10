def is_valid(cards):
    if len(cards) != len(set(cards)):
        return False
    return True

if __name__ == '__main__':
    is_valid()