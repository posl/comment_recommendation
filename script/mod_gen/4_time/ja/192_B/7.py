def isDifficultString(s):
    if s[0::2].isupper() and s[1::2].islower():
        return True
    else:
        return False

if __name__ == '__main__':
    isDifficultString()