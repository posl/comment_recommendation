def calc(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return 26 * calc(s[:-1]) + ord(s[-1]) - ord('A') + 1
