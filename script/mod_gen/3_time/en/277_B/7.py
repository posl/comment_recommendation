def is_valid(s):
    if s[0] in 'HDCK' and s[1] in 'A23456789TJQK':
        return True
    else:
        return False

if __name__ == '__main__':
    is_valid()