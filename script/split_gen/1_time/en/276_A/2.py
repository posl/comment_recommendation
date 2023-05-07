def find_last_occurrence(str, ch):
    for i in range(len(str)-1, -1, -1):
        if str[i] == ch:
            return i + 1
    return -1
