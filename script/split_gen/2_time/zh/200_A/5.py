def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
