def is_good_string(s):
    #print(s)
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if len(s) == 2:
        if s == "()":
            return True
        else:
            return False
    if len(s) == 3:
        if s == "a()":
            return True
        else:
            return False
    if len(s) == 4:
        if s == "ab()":
            return True
        else:
            return False
    if len(s) == 5:
        if s == "aba()":
            return True
        else:
            return False
    if len(s) == 6:
        if s == "abab()":
            return True
        else:
            return False
    if len(s) == 7:
        if s == "ababa()":
            return True
        else:
            return False
    if len(s) == 8:
        if s == "ababab()":
            return True
        else:
            return False
    if len(s) == 9:
        if s == "abababa()":
            return True
        else:
            return False
    if len(s) == 10:
        if s == "abababab()":
            return True
        else:
            return False
    if len(s) == 11:
        if s == "ababababa()":
            return True
        else:
            return False
    if len(s) == 12:
        if s == "ababababab()":
            return True
        else:
            return False
    if len(s) == 13:
        if s == "abababababa()":
            return True
        else:
            return False
    if len(s) == 14:
        if s == "abababababab()":
            return True
        else:
            return False
    if len(s) == 15:
        if s == "ababababababa()":
            return True
        else:
            return False
    if len(s) == 16:
        if s == "ababababababab()":
            return True
        else:
            return False
    if len(s) == 17:

if __name__ == '__main__':
    is_good_string()