def check_hands(hands):
    #print(hands)
    if len(hands) != 2:
        return False
    if hands[0] not in ['H','D','C','S']:
        return False
    if hands[1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        return False
    return True
