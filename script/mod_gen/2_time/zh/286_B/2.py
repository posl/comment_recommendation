def replace_na(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == 'n' and s[i+1] == 'a':
            s = s[:i] + 'ny' + s[i+2:]
        i += 1
    return s

if __name__ == '__main__':
    replace_na()