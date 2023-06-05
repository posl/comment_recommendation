def replace_na(s):
    if len(s) < 2:
        return s
    else:
        if s[0:2] == 'na':
            return 'nya' + replace_na(s[2:])
        else:
            return s[0] + replace_na(s[1:])
