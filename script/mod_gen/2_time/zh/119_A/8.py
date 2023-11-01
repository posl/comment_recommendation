def is_heisei(s):
    year, month, day = map(int, s.split("/"))
    if year < 2019:
        return True
    elif ye

if __name__ == '__main__':
    is_heisei()