def split_check(s):
    if s[0] == '0':
        return 'No'
    for i in range(1, 5):
        if s[i] == '0' and s[10 - i] == '0':
            return 'No'
    return 'Yes'
