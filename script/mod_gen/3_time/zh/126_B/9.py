def check_yymm(s):
    if int(s[2:]) <= 12 and int(s[2:]) >= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    check_yymm()