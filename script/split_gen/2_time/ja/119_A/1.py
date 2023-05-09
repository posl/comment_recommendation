def is_heisei(year, month, day):
    if year > 2019:
        return False
    elif year == 2019 and month > 4:
        return False
    elif year == 2019 and month == 4 and day > 30:
        return False
    return True
