def find_uniq_char(s):
    if s[0] == s[1]:
        return s[2]
    elif s[0] == s[2]:
        return s[1]
    else:
        return s[0]

if __name__ == '__main__':
    find_uniq_char()