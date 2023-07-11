def is_heisei(s):
    year, month, day = map(int, s.split("/"))
    if year < 2019:
        return True
    elif ye
