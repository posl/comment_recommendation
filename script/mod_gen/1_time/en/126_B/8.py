def check_yymm(s):
    year = int(s[0:2])
    month = int(s[2:4])
    if month >= 1 and month <= 12:
        return True
    else:
        return False

if __name__ == '__main__':
    check_yymm()