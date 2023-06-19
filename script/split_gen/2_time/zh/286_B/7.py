def replace_na(s):
    if len(s) <= 1:
        return s
    elif len(s) == 2 and s == 'na':
        return 'nya'
    else:
        result = ''
        for i in range(len(s)):
            if s[i] == 'n' and i < len(s) - 1 and s[i + 1] == 'a':
                result += 'nya'
            else:
                result += s[i]
        return result
