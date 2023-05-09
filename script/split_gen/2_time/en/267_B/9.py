def isSplit(placement):
    #print(placement)
    if placement[0] == '0':
        return False
    if placement[1] == '1' and placement[2] == '1' and placement[3] == '1' and placement[4] == '1':
        return False
    if placement[5] == '1' and placement[6] == '1' and placement[7] == '1' and placement[8] == '1':
        return False
    if placement[1] == '0' and placement[5] == '0':
        return False
    if placement[2] == '0' and placement[6] == '0':
        return False
    if placement[3] == '0' and placement[7] == '0':
        return False
    if placement[4] == '0' and placement[8] == '0':
        return False
    return True
placement = input()
