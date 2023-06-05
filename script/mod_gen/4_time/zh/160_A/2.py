def is_coffee(s):
    if len(s) != 6:
        return False
    if s[2] == s[3] and s[4] == s[5]:
        return True
    return False

if __name__ == '__main__':
    is_coffee()