def replace_na(s):
    if len(s) < 3:
        return s
    if s[0] == 'n' and s[1] == 'a':
        return 'nya' + replace_na(s[2:])
    else:
        return s[0] + replace_na(s[1:])

if __name__ == '__main__':
    replace_na()