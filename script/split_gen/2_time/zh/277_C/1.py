def check_card(s):
    if len(s) != 2:
        return False
    if s[0] not in "HDCS":
        return False
    if s[1] not in "A23456789TJQK":
        return False
    return True
