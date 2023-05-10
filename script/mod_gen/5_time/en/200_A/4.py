def century(year):
    century = year // 100
    if year % 100 == 0:
        return century
    else:
        return century + 1

if __name__ == '__main__':
    century()