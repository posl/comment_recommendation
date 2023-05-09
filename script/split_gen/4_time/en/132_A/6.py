def isSameChar(str):
    if str[0] == str[1] and str[2] == str[3] and str[0] != str[2]:
        return True
    elif str[0] == str[2] and str[1] == str[3] and str[0] != str[1]:
        return True
    elif str[0] == str[3] and str[1] == str[2] and str[0] != str[1]:
        return True
    else:
        return False
