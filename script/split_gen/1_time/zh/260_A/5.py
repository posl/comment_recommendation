def single_char(str):
    if len(str) != 3:
        return -1
    else:
        if str[0] == str[1]:
            return str[2]
        elif str[0] == str[2]:
            return str[1]
        elif str[1] == str[2]:
            return str[0]
        else:
            return -1
