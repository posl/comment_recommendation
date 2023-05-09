def judge_heisei(year, month, day):
    if year > 2019:
        return False
    elif year == 2019:
        if month > 4:
            return False
        elif month == 4:
            if day > 30:
                return False
    return True
