def find_unique_char(s):
    if s[0] != s[1] and s[0] != s[2]:
        return s[0]
    elif s[1] != s[0] and s[1] != s[2]:
        return s[1]
    elif s[2] != s[0] and s[2] != s[1]:
        return s[2]
    else:
        return -1

if __name__ == '__main__':
    find_unique_char()