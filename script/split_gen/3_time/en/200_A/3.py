def century_from_year(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century
