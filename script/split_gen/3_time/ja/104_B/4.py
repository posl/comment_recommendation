def is_ac(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for i in range(len(s)):
        if i == 0:
            continue
        elif i == 1:
            if s[i] != 'C':
                if s[i].isupper():
                    return False
                else:
                    continue
            else:
                return False
        elif i == len(s)-1:
            if s[i].isupper():
                return False
            else:
                continue
        else:
            if s[i].isupper():
                return False
            else:
                continue
    return True
