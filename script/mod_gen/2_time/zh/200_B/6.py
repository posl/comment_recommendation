def century_from_year(year):
    century = 0
    if year % 100 == 0:
        century = year // 100
    else:
        century = year // 100 + 1
    return century

if __name__ == '__main__':
    century_from_year()