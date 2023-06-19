def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

if __name__ == '__main__':
    century_from_year()