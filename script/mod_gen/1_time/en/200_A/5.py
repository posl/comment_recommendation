def century_from_year(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century

if __name__ == '__main__':
    century_from_year()